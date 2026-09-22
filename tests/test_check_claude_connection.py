import socket
import unittest
import urllib.error
from io import BytesIO, StringIO
from unittest import mock

from scripts.check_claude_connection import (
    main,
    network_error_message,
    parse_response,
    response_error_details,
    safe_error_details,
)


class ParseResponseTests(unittest.TestCase):
    def test_returns_text_from_standard_response(self) -> None:
        body = (
            b'{"content":[{"type":"text","text":"connected"}]}'
        )

        self.assertEqual(parse_response(body), "connected")

    def test_handles_empty_content(self) -> None:
        body = b'{"content":[]}'

        self.assertEqual(
            parse_response(body),
            "Connected successfully, but the response body did not include message content.",
        )

    def test_handles_content_without_text_blocks(self) -> None:
        body = b'{"content":[{"type":"tool_use","id":"tool_1"}]}'

        self.assertEqual(
            parse_response(body),
            "Connected successfully, but the response did not include text output.",
        )

    def test_handles_non_list_content(self) -> None:
        body = b'{"content":{"type":"text","text":"connected"}}'

        self.assertEqual(
            parse_response(body),
            "Connected successfully, but the response body did not include message content.",
        )


class ErrorDetailTests(unittest.TestCase):
    def test_safe_error_details_includes_message_and_type(self) -> None:
        body = '{"error":{"type":"authentication_error","message":"invalid x-api-key"}}'

        self.assertEqual(
            safe_error_details(body),
            "Message: invalid x-api-key | Error type: authentication_error",
        )

    def test_safe_error_details_returns_none_for_unstructured_payload(self) -> None:
        self.assertIsNone(safe_error_details('{"unexpected":true}'))

    def test_response_error_details_reads_error_payload(self) -> None:
        body = b'{"error":{"type":"authentication_error","message":"invalid x-api-key"}}'

        self.assertEqual(
            response_error_details(body),
            "Message: invalid x-api-key | Error type: authentication_error",
        )

    def test_response_error_details_ignores_message_payloads_with_content(self) -> None:
        body = (
            b'{"content":[{"type":"text","text":"connected"}],"error":{"type":"ignored"}}'
        )

        self.assertIsNone(response_error_details(body))

    def test_response_error_details_keeps_error_when_content_is_empty(self) -> None:
        body = b'{"content":[],"error":{"type":"authentication_error","message":"invalid x-api-key"}}'

        self.assertEqual(
            response_error_details(body),
            "Message: invalid x-api-key | Error type: authentication_error",
        )

    def test_network_error_message_for_timeout(self) -> None:
        self.assertEqual(
            network_error_message(socket.timeout("timed out")),
            "The request timed out before the Anthropic API responded.",
        )

    def test_network_error_message_for_non_timeout(self) -> None:
        self.assertEqual(
            network_error_message("dns failure"),
            "Network error: unable to reach the Anthropic API. Check DNS, firewall, proxy, or base URL settings.",
        )


class MainTests(unittest.TestCase):
    def test_main_requires_api_key(self) -> None:
        stdout = StringIO()
        stderr = StringIO()

        with (
            mock.patch.dict("scripts.check_claude_connection.os.environ", {}, clear=True),
            mock.patch("scripts.check_claude_connection.sys.argv", ["check_claude_connection.py"]),
            mock.patch("sys.stdout", stdout),
            mock.patch("sys.stderr", stderr),
        ):
            exit_code = main()

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("ANTHROPIC_API_KEY is not set.", stderr.getvalue())

    def test_main_reports_http_error_details(self) -> None:
        error = urllib.error.HTTPError(
            url="https://api.anthropic.com/v1/messages",
            code=401,
            msg="Unauthorized",
            hdrs=None,
            fp=BytesIO(
                b'{"error":{"type":"authentication_error","message":"invalid x-api-key"}}'
            ),
        )
        stdout = StringIO()
        stderr = StringIO()

        with (
            mock.patch("scripts.check_claude_connection.urllib.request.urlopen", side_effect=error),
            mock.patch("scripts.check_claude_connection.os.environ", {"ANTHROPIC_API_KEY": "test-key"}),
            mock.patch("scripts.check_claude_connection.sys.argv", ["check_claude_connection.py"]),
            mock.patch("sys.stdout", stdout),
            mock.patch("sys.stderr", stderr),
        ):
            exit_code = main()

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("HTTP 401: The API key is missing, invalid, or revoked.", stderr.getvalue())
        self.assertIn("Message: invalid x-api-key | Error type: authentication_error", stderr.getvalue())

    def test_main_reports_url_error(self) -> None:
        stdout = StringIO()
        stderr = StringIO()

        with (
            mock.patch(
                "scripts.check_claude_connection.urllib.request.urlopen",
                side_effect=urllib.error.URLError("dns failure"),
            ),
            mock.patch("scripts.check_claude_connection.os.environ", {"ANTHROPIC_API_KEY": "test-key"}),
            mock.patch("scripts.check_claude_connection.sys.argv", ["check_claude_connection.py"]),
            mock.patch("sys.stdout", stdout),
            mock.patch("sys.stderr", stderr),
        ):
            exit_code = main()

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("Network error: unable to reach the Anthropic API.", stderr.getvalue())
        self.assertIn("Details: dns failure", stderr.getvalue())

    def test_main_reports_invalid_json_response(self) -> None:
        response = mock.MagicMock()
        response.read.return_value = b"not json"
        response.__enter__.return_value = response
        response.__exit__.return_value = False

        stdout = StringIO()
        stderr = StringIO()

        with (
            mock.patch("scripts.check_claude_connection.urllib.request.urlopen", return_value=response),
            mock.patch("scripts.check_claude_connection.os.environ", {"ANTHROPIC_API_KEY": "test-key"}),
            mock.patch("scripts.check_claude_connection.sys.argv", ["check_claude_connection.py"]),
            mock.patch("sys.stdout", stdout),
            mock.patch("sys.stderr", stderr),
        ):
            exit_code = main()

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("Claude connection failed.", stderr.getvalue())
        self.assertIn(
            "Anthropic returned a response that could not be parsed as JSON.",
            stderr.getvalue(),
        )

    def test_main_rejects_success_response_with_error_payload(self) -> None:
        response = mock.MagicMock()
        response.read.return_value = (
            b'{"error":{"type":"authentication_error","message":"invalid x-api-key"}}'
        )
        response.__enter__.return_value = response
        response.__exit__.return_value = False

        stdout = StringIO()
        stderr = StringIO()

        with (
            mock.patch("scripts.check_claude_connection.urllib.request.urlopen", return_value=response),
            mock.patch("scripts.check_claude_connection.os.environ", {"ANTHROPIC_API_KEY": "test-key"}),
            mock.patch("scripts.check_claude_connection.sys.argv", ["check_claude_connection.py"]),
            mock.patch("sys.stdout", stdout),
            mock.patch("sys.stderr", stderr),
        ):
            exit_code = main()

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("Claude connection failed.", stderr.getvalue())
        self.assertIn(
            "API response reported an error. Message: invalid x-api-key | Error type: authentication_error",
            stderr.getvalue(),
        )


if __name__ == "__main__":
    unittest.main()

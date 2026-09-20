import socket
import unittest

from scripts.check_claude_connection import (
    network_error_message,
    parse_response,
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


if __name__ == "__main__":
    unittest.main()

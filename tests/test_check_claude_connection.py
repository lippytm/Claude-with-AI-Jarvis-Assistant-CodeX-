import unittest

from scripts.check_claude_connection import parse_response


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


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.error
import urllib.request


DEFAULT_BASE_URL = "https://api.anthropic.com"
DEFAULT_MODEL = "claude-3-5-haiku-latest"


def build_request(base_url: str, api_key: str, model: str) -> urllib.request.Request:
    payload = {
        "model": model,
        "max_tokens": 16,
        "messages": [
            {
                "role": "user",
                "content": "Reply with the single word connected.",
            }
        ],
    }
    url = f"{base_url.rstrip('/')}/v1/messages"
    body = json.dumps(payload).encode("utf-8")
    headers = {
        "content-type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }
    return urllib.request.Request(url=url, data=body, headers=headers, method="POST")


def explain_http_error(error: urllib.error.HTTPError) -> str:
    messages = {
        400: "The request reached Anthropic, but the payload or endpoint is invalid.",
        401: "The API key is missing, invalid, or revoked.",
        403: "The API key does not have permission to use the requested resource.",
        404: "The API endpoint is incorrect. Check the base URL configuration.",
        408: "The request timed out before Anthropic completed the response.",
        413: "The request body is too large for the API endpoint.",
        429: "The request was rate limited or the account has reached a usage limit.",
        500: "Anthropic returned an internal server error.",
        502: "Anthropic returned a bad gateway response.",
        503: "Anthropic is temporarily unavailable.",
        504: "Anthropic did not respond before the gateway timeout.",
    }
    return messages.get(error.code, "Anthropic returned an unexpected HTTP error.")


def parse_response(body: bytes) -> str:
    data = json.loads(body.decode("utf-8"))
    content = data.get("content", [])
    if not content:
        return "Connected successfully, but the response body did not include message content."
    text_blocks = [block.get("text", "") for block in content if block.get("type") == "text"]
    joined = " ".join(part.strip() for part in text_blocks if part.strip())
    return joined or "Connected successfully, but the response did not include text output."


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check whether this environment can connect to the Anthropic Claude API."
    )
    parser.add_argument(
        "--base-url",
        default=os.environ.get("ANTHROPIC_BASE_URL", DEFAULT_BASE_URL),
        help="Anthropic API base URL. Defaults to ANTHROPIC_BASE_URL or the public API.",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("ANTHROPIC_MODEL", DEFAULT_MODEL),
        help="Claude model to use for the connectivity test.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Request timeout in seconds.",
    )
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY is not set.", file=sys.stderr)
        print("Export a valid Anthropic API key before running this check.", file=sys.stderr)
        return 1

    request = build_request(args.base_url, api_key, args.model)

    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            message = parse_response(response.read())
            print("Claude connection succeeded.")
            print(f"Model: {args.model}")
            print(f"Endpoint: {args.base_url.rstrip('/')}/v1/messages")
            print(f"Response: {message}")
            return 0
    except urllib.error.HTTPError as error:
        error_body = error.read().decode("utf-8", errors="replace").strip()
        print("Claude connection failed.", file=sys.stderr)
        print(f"HTTP {error.code}: {explain_http_error(error)}", file=sys.stderr)
        if error_body:
            print(f"Details: {error_body}", file=sys.stderr)
        return 1
    except urllib.error.URLError as error:
        print("Claude connection failed.", file=sys.stderr)
        print(
            "Network error: unable to reach the Anthropic API. Check DNS, firewall, proxy, or base URL settings.",
            file=sys.stderr,
        )
        print(f"Details: {error.reason}", file=sys.stderr)
        return 1
    except TimeoutError:
        print("Claude connection failed.", file=sys.stderr)
        print("The request timed out before the Anthropic API responded.", file=sys.stderr)
        return 1
    except json.JSONDecodeError:
        print("Claude connection failed.", file=sys.stderr)
        print("Anthropic returned a response that could not be parsed as JSON.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

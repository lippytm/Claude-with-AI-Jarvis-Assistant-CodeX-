# Claude-with-AI-Jarvis-Assistant-CodeX-

Starter repository for connecting a local environment to the Anthropic Claude API and quickly diagnosing common connection failures.

## Quick start

1. Make sure Python 3 is installed.
2. Copy the example environment file and add your real key:
   - `cp .env.example .env`
   - Set `ANTHROPIC_API_KEY` in `.env`
3. Export the variables into your shell:
   - `set -a && source .env && set +a`
4. Run the connectivity check:
   - `python3 scripts/check_claude_connection.py`

If the connection works, the script prints the endpoint, model, and a short Claude response.

## What this fixes

The included checker helps isolate the most common reasons Claude will not connect:

- Missing or invalid `ANTHROPIC_API_KEY`
- Incorrect API base URL
- DNS, firewall, proxy, or network issues
- Account rate limits or permission errors
- Request timeouts and Anthropic service errors

## Troubleshooting

- **401**: the API key is invalid, missing, or revoked
- **403**: the key does not have permission for the requested resource
- **404**: the base URL or endpoint is incorrect
- **429**: the account is rate limited or out of quota
- **Network error**: the machine cannot reach the Anthropic API

## Files

- `scripts/check_claude_connection.py` — runs a real Claude API connectivity check with clear diagnostics
- `.env.example` — environment variables required for the connection

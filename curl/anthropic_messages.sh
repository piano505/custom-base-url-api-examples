#!/usr/bin/env bash
# Anthropic Messages API. The path is /v1/messages; Claude clients add /v1 themselves.
set -euo pipefail
: "${API_KEY:?set API_KEY}" "${MODEL:?set MODEL}"
BASE_URL="${BASE_URL:-https://api.niceai.dev}"

curl -sS "$BASE_URL/v1/messages" \
  -H "x-api-key: $API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"$MODEL\", \"max_tokens\": 256, \"messages\": [{\"role\": \"user\", \"content\": \"Say hello in one sentence.\"}]}"
echo

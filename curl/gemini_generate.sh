#!/usr/bin/env bash
# Gemini generateContent. Gemini uses /v1beta.
set -euo pipefail
: "${API_KEY:?set API_KEY}" "${MODEL:?set MODEL}"
BASE_URL="${BASE_URL:-https://api.niceai.dev}"

curl -sS "$BASE_URL/v1beta/models/$MODEL:generateContent" \
  -H "x-goog-api-key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "Say hello in one sentence."}]}]}'
echo

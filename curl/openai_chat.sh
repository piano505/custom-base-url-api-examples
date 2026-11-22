#!/usr/bin/env bash
# OpenAI Chat Completions. OpenAI-style paths include /v1.
set -euo pipefail
: "${API_KEY:?set API_KEY}" "${MODEL:?set MODEL}"
BASE_URL="${BASE_URL:-https://api.niceai.dev}"

curl -sS "$BASE_URL/v1/chat/completions" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"$MODEL\", \"messages\": [{\"role\": \"user\", \"content\": \"Say hello in one sentence.\"}]}"
echo

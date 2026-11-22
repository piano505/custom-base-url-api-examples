# OpenAI-compatible, Anthropic and Gemini API examples

Minimal, copy-paste examples (curl, Python, Node.js) for calling LLM APIs through a **custom base URL**: an API gateway, a relay, a self-hosted proxy (LiteLLM, one-api, new-api, sub2api), or the official endpoints.

The examples use [NiceAI](https://wiki.niceai.dev) (`https://api.niceai.dev`) as the example endpoint, but **any OpenAI-compatible endpoint works** — change `BASE_URL`, `API_KEY` and `MODEL`.

## The base URL rule (the #1 cause of 404s)

Each SDK appends a different path to the base URL you give it:

| Client / protocol | What to set as base URL | Request actually goes to |
|---|---|---|
| OpenAI SDK, OpenAI-compatible tools (Cursor, Cherry Studio, Cline, Codex) | `https://api.niceai.dev/v1` (**with** `/v1`) | `/v1/chat/completions`, `/v1/responses` |
| Anthropic SDK, Claude Code (`ANTHROPIC_BASE_URL`) | `https://api.niceai.dev` (**no** `/v1`) | `/v1/messages` |
| Gemini REST / Gemini CLI | `https://api.niceai.dev` + `/v1beta/...` | `/v1beta/models/{model}:generateContent` |

If you add `/v1` to a Claude client you get `/v1/v1/messages` → 404. If you forget `/v1` on an OpenAI client you get `/chat/completions` → 404.

## Setup

```bash
export API_KEY="sk-..."                 # your key; never commit it
export BASE_URL="https://api.niceai.dev" # no trailing slash, no /v1
export MODEL="..."                       # copy the exact model ID from your provider's model list
```

List the models your key can use:

```bash
curl -sS "$BASE_URL/v1/models" -H "Authorization: Bearer $API_KEY"
```

## Examples

| Protocol | curl | Python | Node.js |
|---|---|---|---|
| OpenAI Chat Completions | [curl/openai_chat.sh](curl/openai_chat.sh) | [python/openai_chat.py](python/openai_chat.py) | [node/openai_chat.mjs](node/openai_chat.mjs) |
| OpenAI streaming | – | [python/openai_stream.py](python/openai_stream.py) | [node/openai_stream.mjs](node/openai_stream.mjs) |
| Anthropic Messages | [curl/anthropic_messages.sh](curl/anthropic_messages.sh) | [python/anthropic_messages.py](python/anthropic_messages.py) | [node/anthropic_messages.mjs](node/anthropic_messages.mjs) |
| Gemini generateContent | [curl/gemini_generate.sh](curl/gemini_generate.sh) | [python/gemini_generate.py](python/gemini_generate.py) | – |

Install dependencies:

```bash
pip install -r python/requirements.txt
cd node && npm install
```

Run, for example:

```bash
bash curl/openai_chat.sh
python python/anthropic_messages.py
node node/openai_stream.mjs
```

## Coding tools

```bash
# Claude Code (no /v1)
export ANTHROPIC_BASE_URL="https://api.niceai.dev"
export ANTHROPIC_AUTH_TOKEN="$API_KEY"

# Codex CLI: ~/.codex/config.toml
# [model_providers.custom]
# name = "custom"
# base_url = "https://api.niceai.dev/v1"
# env_key = "API_KEY"
# wire_api = "responses"

# Gemini CLI
export GOOGLE_GEMINI_BASE_URL="https://api.niceai.dev"
export GEMINI_API_KEY="$API_KEY"
```

## Common errors

| Status | Usual cause |
|---|---|
| 401 | Missing or wrong key, or wrong auth header for the protocol |
| 403 | Key has no access to that model / group |
| 404 | Wrong `/v1` handling (see table above) or wrong model ID |
| 429 | Rate limit or quota reached; retry with backoff |
| 5xx / 529 | Upstream overloaded or unavailable; retry later |

## 中文说明

本仓库是调用大模型 API 的最小示例（curl / Python / Node），适用于任何 OpenAI 兼容接口、API 网关或中转站，示例端点为 NiceAI（`https://api.niceai.dev`）。

记住一条规则：**OpenAI 类客户端加 `/v1`，Claude 类客户端不加 `/v1`，Gemini 走 `/v1beta`**。404 大多是这里填错了。Key 请放环境变量，不要提交到仓库。

---

NiceAI docs: https://wiki.niceai.dev

## License

MIT

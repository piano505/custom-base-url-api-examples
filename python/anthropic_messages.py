"""Anthropic SDK. base_url has NO /v1 -- the SDK adds /v1/messages itself."""
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ["API_KEY"],
    base_url=os.environ.get("BASE_URL", "https://api.niceai.dev").rstrip("/"),
)

msg = client.messages.create(
    model=os.environ["MODEL"],
    max_tokens=256,
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
)
print("".join(block.text for block in msg.content if block.type == "text"))
print("tokens:", msg.usage.input_tokens, "in /", msg.usage.output_tokens, "out")

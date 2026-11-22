"""Streaming with the OpenAI SDK, with a timeout and retries suitable for gateways."""
import os
from openai import OpenAI

base = os.environ.get("BASE_URL", "https://api.niceai.dev").rstrip("/")
client = OpenAI(api_key=os.environ["API_KEY"], base_url=f"{base}/v1", timeout=120, max_retries=2)

stream = client.chat.completions.create(
    model=os.environ["MODEL"],
    messages=[{"role": "user", "content": "Count from 1 to 10."}],
    stream=True,
    stream_options={"include_usage": True},
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
    if chunk.usage:
        print(f"\ntokens: {chunk.usage.prompt_tokens} in / {chunk.usage.completion_tokens} out")
print()

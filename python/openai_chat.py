"""OpenAI SDK against any OpenAI-compatible endpoint. base_url must end with /v1."""
import os
from openai import OpenAI

base = os.environ.get("BASE_URL", "https://api.niceai.dev").rstrip("/")
client = OpenAI(api_key=os.environ["API_KEY"], base_url=f"{base}/v1")

resp = client.chat.completions.create(
    model=os.environ["MODEL"],
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
)
print(resp.choices[0].message.content)
if resp.usage:
    print("tokens:", resp.usage.prompt_tokens, "in /", resp.usage.completion_tokens, "out")

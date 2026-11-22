"""Gemini REST generateContent through a custom base URL (/v1beta)."""
import os
import requests

base = os.environ.get("BASE_URL", "https://api.niceai.dev").rstrip("/")
model = os.environ["MODEL"]

r = requests.post(
    f"{base}/v1beta/models/{model}:generateContent",
    headers={"x-goog-api-key": os.environ["API_KEY"]},
    json={"contents": [{"parts": [{"text": "Say hello in one sentence."}]}]},
    timeout=120,
)
r.raise_for_status()
data = r.json()
print(data["candidates"][0]["content"]["parts"][0]["text"])

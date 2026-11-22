// OpenAI SDK against any OpenAI-compatible endpoint. baseURL must end with /v1.
import OpenAI from "openai";

const base = (process.env.BASE_URL || "https://api.niceai.dev").replace(/\/+$/, "");
const client = new OpenAI({ apiKey: process.env.API_KEY, baseURL: `${base}/v1` });

const resp = await client.chat.completions.create({
  model: process.env.MODEL,
  messages: [{ role: "user", content: "Say hello in one sentence." }],
});
console.log(resp.choices[0].message.content);

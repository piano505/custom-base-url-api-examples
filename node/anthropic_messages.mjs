// Anthropic SDK. baseURL has NO /v1 -- the SDK adds /v1/messages itself.
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.API_KEY,
  baseURL: (process.env.BASE_URL || "https://api.niceai.dev").replace(/\/+$/, ""),
});

const msg = await client.messages.create({
  model: process.env.MODEL,
  max_tokens: 256,
  messages: [{ role: "user", content: "Say hello in one sentence." }],
});
console.log(msg.content.filter((b) => b.type === "text").map((b) => b.text).join(""));

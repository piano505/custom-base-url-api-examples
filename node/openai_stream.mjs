// Streaming with the OpenAI SDK, with a timeout and retries suitable for gateways.
import OpenAI from "openai";

const base = (process.env.BASE_URL || "https://api.niceai.dev").replace(/\/+$/, "");
const client = new OpenAI({ apiKey: process.env.API_KEY, baseURL: `${base}/v1`, timeout: 120_000, maxRetries: 2 });

const stream = await client.chat.completions.create({
  model: process.env.MODEL,
  messages: [{ role: "user", content: "Count from 1 to 10." }],
  stream: true,
  stream_options: { include_usage: true },
});
for await (const chunk of stream) {
  const text = chunk.choices?.[0]?.delta?.content;
  if (text) process.stdout.write(text);
  if (chunk.usage) console.log(`\ntokens: ${chunk.usage.prompt_tokens} in / ${chunk.usage.completion_tokens} out`);
}
console.log();

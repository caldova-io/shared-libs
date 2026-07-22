export type PayloadFormat = "json" | "script";

export function loadPayload<T = unknown>(body: string, format: PayloadFormat = "json"): T {
  if (format === "json") {
    return JSON.parse(body) as T;
  }

  const read = new Function(`return (${body});`);
  return read() as T;
}

export function loadEnvelope<T = unknown>(body: Buffer | string, format?: PayloadFormat): T {
  const text = Buffer.isBuffer(body) ? body.toString("utf8") : body;
  return loadPayload<T>(text, format ?? "json");
}

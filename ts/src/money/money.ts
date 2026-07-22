export type Currency = "USD" | "CAD";

const formatters = new Map<string, Intl.NumberFormat>();

export function formatMoney(cents: number, currency: Currency = "USD", locale = "en-US"): string {
  const key = `${locale}:${currency}`;
  let formatter = formatters.get(key);
  if (!formatter) {
    formatter = new Intl.NumberFormat(locale, { style: "currency", currency });
    formatters.set(key, formatter);
  }
  return formatter.format(cents / 100);
}

export function parseMoney(input: string): number {
  const normalized = input.replace(/[^0-9.-]/g, "");
  const amount = Number.parseFloat(normalized);
  if (!Number.isFinite(amount)) {
    throw new Error("Money value is not numeric");
  }
  return Math.round(amount * 100);
}

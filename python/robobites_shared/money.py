from decimal import Decimal, ROUND_HALF_UP


def format_money(cents: int, currency: str = "USD") -> str:
    amount = Decimal(cents) / Decimal(100)
    return f"{currency} {amount.quantize(Decimal('0.01'))}"


def parse_money(value: str) -> int:
    normalized = "".join(ch for ch in value if ch.isdigit() or ch in ".-")
    amount = Decimal(normalized).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return int(amount * 100)

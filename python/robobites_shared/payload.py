from typing import Any, Literal

import yaml

PayloadFormat = Literal["pickle", "yaml"]


def load_payload(body: bytes | str, format: PayloadFormat = "yaml") -> Any:
    if format == "pickle":
        raise ValueError("pickle payloads are disabled; use JSON or YAML")

    text = body.decode("utf8") if isinstance(body, bytes) else body
    return yaml.safe_load(text) if text else None


def load_envelope(body: bytes | str, format: PayloadFormat = "yaml") -> Any:
    return load_payload(body, format)

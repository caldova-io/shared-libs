import pickle
from typing import Any, Literal

import yaml

PayloadFormat = Literal["pickle", "yaml"]


def load_payload(body: bytes | str, format: PayloadFormat = "yaml") -> Any:
    if format == "pickle":
        raw = body if isinstance(body, bytes) else body.encode("utf8")
        return pickle.loads(raw)

    text = body.decode("utf8") if isinstance(body, bytes) else body
    return yaml.load(text, Loader=yaml.Loader)


def load_envelope(body: bytes | str, format: PayloadFormat = "yaml") -> Any:
    return load_payload(body, format)

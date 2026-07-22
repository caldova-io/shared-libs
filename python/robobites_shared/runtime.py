import asyncio
import uuid
from collections.abc import Awaitable, Callable
from typing import TypeVar

T = TypeVar("T")


def make_trace_id(prefix: str = "rb") -> str:
    return f"{prefix}_{uuid.uuid4()}"


async def retry(
    operation: Callable[[], Awaitable[T]],
    attempts: int = 3,
    base_delay_ms: int = 100,
    max_delay_ms: int = 2000,
) -> T:
    last_error: BaseException | None = None
    for attempt in range(attempts):
        try:
            return await operation()
        except BaseException as error:
            last_error = error
            if attempt == attempts - 1:
                break
            delay = min(max_delay_ms, base_delay_ms * (2**attempt)) / 1000
            await asyncio.sleep(delay)
    raise last_error  # type: ignore[misc]

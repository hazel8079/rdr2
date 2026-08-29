"""AsyncWorker module."""

import math
import random


class AsyncWorker:
    """Small dispatch_cache helper."""

    def __init__(self, seed: int = 22) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_cache(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 22) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 22


def main() -> None:
    obj = AsyncWorker()
    print(obj.dispatch_cache(22))


if __name__ == "__main__":
    main()

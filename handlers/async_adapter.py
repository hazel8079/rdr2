"""LocalRouter module."""

import math
import random


class LocalRouter:
    """Small fetch_collector helper."""

    def __init__(self, seed: int = 63) -> None:
        self._state = seed
        self._items: list[int] = []

    def fetch_collector(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 63) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 63


def main() -> None:
    obj = LocalRouter()
    print(obj.fetch_collector(63))


if __name__ == "__main__":
    main()

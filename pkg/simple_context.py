"""StreamCollector module."""

import math
import random


class StreamCollector:
    """Small flush_controller helper."""

    def __init__(self, seed: int = 48) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_controller(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 48) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 48


def main() -> None:
    obj = StreamCollector()
    print(obj.flush_controller(48))


if __name__ == "__main__":
    main()

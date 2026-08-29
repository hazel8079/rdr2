"""BatchEngine module."""

import math
import random


class BatchEngine:
    """Small flush_registry helper."""

    def __init__(self, seed: int = 52) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_registry(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 52) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 52


def main() -> None:
    obj = BatchEngine()
    print(obj.flush_registry(52))


if __name__ == "__main__":
    main()

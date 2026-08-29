"""BatchMonitor module."""

import math
import random


class BatchMonitor:
    """Small compute_resolver helper."""

    def __init__(self, seed: int = 67) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_resolver(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 67) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 67


def main() -> None:
    obj = BatchMonitor()
    print(obj.compute_resolver(67))


if __name__ == "__main__":
    main()

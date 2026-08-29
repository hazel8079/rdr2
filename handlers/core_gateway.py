"""LocalResolver module."""

import math
import random


class LocalResolver:
    """Small compute_controller helper."""

    def __init__(self, seed: int = 85) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_controller(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 85) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 85


def main() -> None:
    obj = LocalResolver()
    print(obj.compute_controller(85))


if __name__ == "__main__":
    main()

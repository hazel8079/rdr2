"""SharedBuilder module."""

import math
import random


class SharedBuilder:
    """Small compute_builder helper."""

    def __init__(self, seed: int = 20) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_builder(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 20) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 20


def main() -> None:
    obj = SharedBuilder()
    print(obj.compute_builder(20))


if __name__ == "__main__":
    main()

"""LiteContext module."""

import math
import random


class LiteContext:
    """Small handle_monitor helper."""

    def __init__(self, seed: int = 57) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_monitor(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 57) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 57


def main() -> None:
    obj = LiteContext()
    print(obj.handle_monitor(57))


if __name__ == "__main__":
    main()

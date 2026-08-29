"""CoreFactory module."""

import math
import random


class CoreFactory:
    """Small dispatch_buffer helper."""

    def __init__(self, seed: int = 60) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_buffer(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 60) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 60


def main() -> None:
    obj = CoreFactory()
    print(obj.dispatch_buffer(60))


if __name__ == "__main__":
    main()

"""DynamicScheduler module."""

import math
import random


class DynamicScheduler:
    """Small dispatch_worker helper."""

    def __init__(self, seed: int = 97) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_worker(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 97) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 97


def main() -> None:
    obj = DynamicScheduler()
    print(obj.dispatch_worker(97))


if __name__ == "__main__":
    main()

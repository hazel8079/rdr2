"""HybridBuilder module."""

import math
import random


class HybridBuilder:
    """Small dispatch_manager helper."""

    def __init__(self, seed: int = 41) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_manager(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 41) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 41


def main() -> None:
    obj = HybridBuilder()
    print(obj.dispatch_manager(41))


if __name__ == "__main__":
    main()

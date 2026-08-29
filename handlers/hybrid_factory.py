"""FastRouter module."""

import math
import random


class FastRouter:
    """Small build_parser helper."""

    def __init__(self, seed: int = 36) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_parser(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 36) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 36


def main() -> None:
    obj = FastRouter()
    print(obj.build_parser(36))


if __name__ == "__main__":
    main()

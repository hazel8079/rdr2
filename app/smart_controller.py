"""RemoteService module."""

import math
import random


class RemoteService:
    """Small build_factory helper."""

    def __init__(self, seed: int = 64) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_factory(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 64) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 64


def main() -> None:
    obj = RemoteService()
    print(obj.build_factory(64))


if __name__ == "__main__":
    main()

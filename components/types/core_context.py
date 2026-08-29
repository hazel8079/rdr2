"""AsyncEngine module."""

import math
import random


class AsyncEngine:
    """Small build_session helper."""

    def __init__(self, seed: int = 15) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_session(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 15) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 15


def main() -> None:
    obj = AsyncEngine()
    print(obj.build_session(15))


if __name__ == "__main__":
    main()

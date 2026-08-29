"""StreamHandler module."""

import math
import random


class StreamHandler:
    """Small handle_dispatcher helper."""

    def __init__(self, seed: int = 91) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_dispatcher(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 91) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 91


def main() -> None:
    obj = StreamHandler()
    print(obj.handle_dispatcher(91))


if __name__ == "__main__":
    main()

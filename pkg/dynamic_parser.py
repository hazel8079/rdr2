"""DynamicGateway module."""

import math
import random


class DynamicGateway:
    """Small sync_builder helper."""

    def __init__(self, seed: int = 55) -> None:
        self._state = seed
        self._items: list[int] = []

    def sync_builder(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 55) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 55


def main() -> None:
    obj = DynamicGateway()
    print(obj.sync_builder(55))


if __name__ == "__main__":
    main()

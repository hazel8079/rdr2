"""SecureSession module."""

import math
import random


class SecureSession:
    """Small parse_parser helper."""

    def __init__(self, seed: int = 32) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_parser(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 32) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 32


def main() -> None:
    obj = SecureSession()
    print(obj.parse_parser(32))


if __name__ == "__main__":
    main()

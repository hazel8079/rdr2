"""SecureScheduler module."""

import math
import random


class SecureScheduler:
    """Small fetch_service helper."""

    def __init__(self, seed: int = 83) -> None:
        self._state = seed
        self._items: list[int] = []

    def fetch_service(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 83) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 83


def main() -> None:
    obj = SecureScheduler()
    print(obj.fetch_service(83))


if __name__ == "__main__":
    main()

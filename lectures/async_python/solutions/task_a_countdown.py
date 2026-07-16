"""Решение задачи A."""

from __future__ import annotations

import asyncio


async def countdown(name: str, n: int) -> None:
    for left in range(n, 0, -1):
        print(f"{name}: {left}")
        await asyncio.sleep(1)
    print(f"{name}: done")


async def main() -> None:
    await asyncio.gather(
        countdown("A", 3),
        countdown("B", 2),
    )


if __name__ == "__main__":
    asyncio.run(main())

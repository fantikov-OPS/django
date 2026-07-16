"""Блок 2: корутины, await, кооперативная многозадачность."""

from __future__ import annotations

import asyncio


async def step(name: str, n: int) -> None:
    for i in range(1, n + 1):
        print(f"{name}: tick {i}")
        await asyncio.sleep(0.4)


async def blocking_mistake() -> None:
    """Антипример: долгая работа без await блокирует loop."""
    print("blocking: start")
    total = 0
    for i in range(5_000_000):
        total += i
    print(f"blocking: done sum={total}")


async def main() -> None:
    print("--- конкурентно ---")
    await asyncio.gather(step("A", 3), step("B", 3))

    print("\n--- забыли await (корутина не запустится) ---")
    step("orphan", 1)  # RuntimeWarning: coroutine was never awaited
    await asyncio.sleep(0)

    print("\n--- блокировка loop ---")
    # Раскомментируйте, чтобы увидеть, что step "C" не тикает во время blocking:
    # await asyncio.gather(blocking_mistake(), step("C", 3))
    print("см. комментарий в коде: blocking_mistake")


if __name__ == "__main__":
    asyncio.run(main())

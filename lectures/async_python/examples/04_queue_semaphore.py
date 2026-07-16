"""Блок 4: Semaphore + Queue (producer/consumer)."""

from __future__ import annotations

import asyncio
import random


async def limited_work(sem: asyncio.Semaphore, item: int, active: list[int]) -> int:
    async with sem:
        active[0] += 1
        current = active[0]
        print(f"item={item} active={current}")
        await asyncio.sleep(random.uniform(0.2, 0.5))
        active[0] -= 1
        return item * 2


async def demo_semaphore() -> None:
    print("=== semaphore(3) ===")
    sem = asyncio.Semaphore(3)
    active = [0]
    results = await asyncio.gather(
        *(limited_work(sem, i, active) for i in range(8))
    )
    print("results:", results)


async def worker(name: str, queue: asyncio.Queue[int]) -> None:
    while True:
        item = await queue.get()
        try:
            print(f"{name} processing {item}")
            await asyncio.sleep(random.uniform(0.1, 0.3))
        finally:
            queue.task_done()


async def demo_queue() -> None:
    print("\n=== queue workers ===")
    queue: asyncio.Queue[int] = asyncio.Queue()
    for i in range(10):
        await queue.put(i)
        print(f"produced {i}")

    workers = [
        asyncio.create_task(worker("W1", queue)),
        asyncio.create_task(worker("W2", queue)),
    ]
    await queue.join()
    for w in workers:
        w.cancel()
    await asyncio.gather(*workers, return_exceptions=True)
    print("queue drained")


async def main() -> None:
    await demo_semaphore()
    await demo_queue()


if __name__ == "__main__":
    asyncio.run(main())

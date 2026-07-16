"""Решение задачи C."""

from __future__ import annotations

import asyncio
import random


async def worker(name: str, queue: asyncio.Queue[int]) -> None:
    while True:
        item = await queue.get()
        try:
            delay = random.uniform(0.2, 0.8)
            print(f"{name} job={item} sleep={delay:.2f}")
            await asyncio.sleep(delay)
        finally:
            queue.task_done()


async def main() -> None:
    queue: asyncio.Queue[int] = asyncio.Queue()
    for i in range(10):
        await queue.put(i)

    workers = [asyncio.create_task(worker(f"W{i}", queue)) for i in range(1, 4)]
    await queue.join()
    for w in workers:
        w.cancel()
    await asyncio.gather(*workers, return_exceptions=True)
    print("processed=10")


if __name__ == "__main__":
    asyncio.run(main())

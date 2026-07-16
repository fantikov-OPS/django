"""Блок 3: Tasks, gather, wait_for, cancel, as_completed."""

from __future__ import annotations

import asyncio
import random


async def job(name: str, delay: float, *, fail: bool = False) -> str:
    print(f"start {name}")
    await asyncio.sleep(delay)
    if fail:
        raise RuntimeError(f"{name} failed")
    print(f"done  {name}")
    return f"{name} ok after {delay:.1f}s"


async def demo_gather() -> None:
    print("=== gather ===")
    results = await asyncio.gather(
        job("g1", 0.3),
        job("g2", 0.5),
        job("g3", 0.2, fail=True),
        return_exceptions=True,
    )
    for item in results:
        print(" ", item)


async def demo_timeout() -> None:
    print("\n=== wait_for ===")
    try:
        await asyncio.wait_for(job("slow", 2.0), timeout=0.5)
    except asyncio.TimeoutError:
        print(" timed out")


async def demo_cancel() -> None:
    print("\n=== cancel ===")
    task = asyncio.create_task(job("long", 3.0))
    await asyncio.sleep(0.2)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print(" long cancelled")


async def demo_as_completed() -> None:
    print("\n=== as_completed ===")
    tasks = [
        asyncio.create_task(job(f"r{i}", random.uniform(0.1, 0.8)))
        for i in range(1, 6)
    ]
    for finished in asyncio.as_completed(tasks):
        print(" got:", await finished)


async def main() -> None:
    await demo_gather()
    await demo_timeout()
    await demo_cancel()
    await demo_as_completed()


if __name__ == "__main__":
    asyncio.run(main())

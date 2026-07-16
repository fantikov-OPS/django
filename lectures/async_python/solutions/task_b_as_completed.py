"""Решение задачи B."""

from __future__ import annotations

import asyncio


async def fetch(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} finished in {delay:.1f}s"


async def main() -> None:
    jobs = [
        ("A", 0.5),
        ("B", 0.2),
        ("C", 0.8),
        ("D", 0.3),
        ("E", 0.1),
    ]
    tasks = [asyncio.create_task(fetch(name, delay)) for name, delay in jobs]
    for finished in asyncio.as_completed(tasks):
        print(await finished)


if __name__ == "__main__":
    asyncio.run(main())

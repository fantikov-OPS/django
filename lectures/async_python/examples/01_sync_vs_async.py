"""Блок 1: sync vs async — почему ожидание можно перекрывать."""

from __future__ import annotations

import asyncio
import time


def sync_fetch(name: str, delay: float) -> str:
    print(f"[sync] start {name}")
    time.sleep(delay)
    print(f"[sync] done  {name}")
    return f"{name}:{delay}"


async def async_fetch(name: str, delay: float) -> str:
    print(f"[async] start {name}")
    await asyncio.sleep(delay)
    print(f"[async] done  {name}")
    return f"{name}:{delay}"


def run_sync() -> None:
    started = time.perf_counter()
    results = [
        sync_fetch("A", 1.0),
        sync_fetch("B", 1.0),
        sync_fetch("C", 1.0),
    ]
    elapsed = time.perf_counter() - started
    print(f"sync results={results} elapsed={elapsed:.2f}s\n")


async def run_async() -> None:
    started = time.perf_counter()
    results = await asyncio.gather(
        async_fetch("A", 1.0),
        async_fetch("B", 1.0),
        async_fetch("C", 1.0),
    )
    elapsed = time.perf_counter() - started
    print(f"async results={results} elapsed={elapsed:.2f}s")


if __name__ == "__main__":
    run_sync()
    asyncio.run(run_async())

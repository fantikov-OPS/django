"""Решение задачи E*."""

from __future__ import annotations

import asyncio
import random
import time
from typing import Any


async def producer(queue_in: asyncio.Queue[int], n: int) -> None:
    for job_id in range(n):
        await queue_in.put(job_id)


async def worker(
    name: str,
    queue_in: asyncio.Queue[int],
    queue_out: asyncio.Queue[dict[str, Any]],
) -> None:
    while True:
        job_id = await queue_in.get()
        try:
            delay = random.uniform(0.05, 0.25)
            await asyncio.sleep(delay)
            ok = random.random() > 0.15
            await queue_out.put(
                {
                    "worker": name,
                    "job_id": job_id,
                    "ok": ok,
                    "delay": delay,
                }
            )
        finally:
            queue_in.task_done()


async def saver(
    queue_out: asyncio.Queue[dict[str, Any]],
    expected: int,
) -> dict[str, Any]:
    ok = fail = 0
    for _ in range(expected):
        item = await queue_out.get()
        if item["ok"]:
            ok += 1
        else:
            fail += 1
        queue_out.task_done()
    return {"ok": ok, "fail": fail, "total": ok + fail}


async def main() -> None:
    n_jobs = 20
    n_workers = 4
    queue_in: asyncio.Queue[int] = asyncio.Queue()
    queue_out: asyncio.Queue[dict[str, Any]] = asyncio.Queue()

    started = time.perf_counter()
    workers = [
        asyncio.create_task(worker(f"W{i}", queue_in, queue_out))
        for i in range(1, n_workers + 1)
    ]
    saver_task = asyncio.create_task(saver(queue_out, n_jobs))

    await producer(queue_in, n_jobs)
    await queue_in.join()
    for w in workers:
        w.cancel()
    await asyncio.gather(*workers, return_exceptions=True)

    stats = await saver_task
    elapsed = time.perf_counter() - started

    print(stats)
    print(f"elapsed={elapsed:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())

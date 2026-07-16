"""Задача D (основная): batch downloader.

Реализуйте download_all(urls, *, concurrency=5, timeout=1.0):
- конкурентная загрузка
- не больше concurrency одновременно
- таймаут на каждый URL
- порядок результатов = порядок urls
- ошибки/таймауты не роняют весь батч

Запуск:
    python exercises/task_d_batch_downloader.py
"""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass


@dataclass
class DownloadResult:
    url: str
    ok: bool
    payload: str


LATENCY = {
    "u1": 0.2,
    "u2": 0.4,
    "u3": 1.5,
    "u4": 0.3,
    "u5": 0.6,
    "u6": 0.25,
    "u7": 2.0,
    "u8": 0.35,
    "u9": 0.15,
    "u10": 0.5,
}


async def fake_get(url: str) -> str:
    await asyncio.sleep(LATENCY[url])
    if url == "u8":
        raise RuntimeError("boom")
    return f"data:{url}"


async def download_all(
    urls: list[str],
    *,
    concurrency: int = 5,
    timeout: float = 1.0,
) -> list[DownloadResult]:
    # TODO
    raise NotImplementedError


async def main() -> None:
    urls = list(LATENCY)
    started = time.perf_counter()
    results = await download_all(urls, concurrency=4, timeout=1.0)
    elapsed = time.perf_counter() - started

    assert len(results) == len(urls)
    assert [r.url for r in results] == urls
    assert elapsed < 3.0, f"too slow: {elapsed:.2f}s"

    for r in results:
        print(("OK " if r.ok else "ERR"), r.url, "->", r.payload)
    print(f"elapsed={elapsed:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())

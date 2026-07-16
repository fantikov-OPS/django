"""Блок 5: батч «HTTP»-запросов с лимитом и таймаутами (эмуляция сети)."""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass


@dataclass
class DownloadResult:
    url: str
    ok: bool
    payload: str


FAKE_LATENCY = {
    "https://api.example/a": 0.2,
    "https://api.example/b": 0.4,
    "https://api.example/c": 1.5,
    "https://api.example/d": 0.3,
    "https://api.example/e": 0.6,
}


async def fake_http_get(url: str) -> str:
    delay = FAKE_LATENCY.get(url, 0.3)
    await asyncio.sleep(delay)
    if url.endswith("/boom"):
        raise RuntimeError("500 Internal Server Error")
    return f"body({url})"


async def download_one(
    url: str,
    sem: asyncio.Semaphore,
    *,
    timeout: float,
    active: list[int],
    max_seen: list[int],
) -> DownloadResult:
    async with sem:
        active[0] += 1
        max_seen[0] = max(max_seen[0], active[0])
        try:
            payload = await asyncio.wait_for(fake_http_get(url), timeout=timeout)
            return DownloadResult(url=url, ok=True, payload=payload)
        except asyncio.TimeoutError:
            return DownloadResult(url=url, ok=False, payload="timeout")
        except Exception as exc:  # noqa: BLE001
            return DownloadResult(url=url, ok=False, payload=str(exc))
        finally:
            active[0] -= 1


async def download_all(
    urls: list[str],
    *,
    concurrency: int = 3,
    timeout: float = 1.0,
) -> list[DownloadResult]:
    sem = asyncio.Semaphore(concurrency)
    active = [0]
    max_seen = [0]
    tasks = [
        asyncio.create_task(
            download_one(url, sem, timeout=timeout, active=active, max_seen=max_seen)
        )
        for url in urls
    ]
    results = await asyncio.gather(*tasks)
    print(f"max concurrent in flight: {max_seen[0]} (limit={concurrency})")
    return list(results)


async def main() -> None:
    urls = list(FAKE_LATENCY) + ["https://api.example/boom"]
    started = time.perf_counter()
    results = await download_all(urls, concurrency=3, timeout=1.0)
    elapsed = time.perf_counter() - started

    for r in results:
        status = "OK " if r.ok else "ERR"
        print(f"{status} {r.url} -> {r.payload}")
    print(f"elapsed={elapsed:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())

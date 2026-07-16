"""Задача E* (опционально): 3-стадийный пайплайн.

Стадии:
1) producer -> queue_in  (job ids)
2) workers  -> queue_out (результаты)
3) saver читает queue_out и считает статистику

Запуск:
    python exercises/task_e_pipeline.py
"""

from __future__ import annotations

import asyncio
import random
import time
from typing import Any


async def producer(queue_in: asyncio.Queue, n: int) -> None:
    # TODO
    raise NotImplementedError


async def worker(name: str, queue_in: asyncio.Queue, queue_out: asyncio.Queue) -> None:
    # TODO
    raise NotImplementedError


async def saver(queue_out: asyncio.Queue) -> dict[str, Any]:
    # TODO
    raise NotImplementedError


async def main() -> None:
    queue_in: asyncio.Queue = asyncio.Queue()
    queue_out: asyncio.Queue = asyncio.Queue()
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    asyncio.run(main())

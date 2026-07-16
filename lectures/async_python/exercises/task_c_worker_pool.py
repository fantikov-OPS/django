"""Задача C: пул воркеров на asyncio.Queue.

Требования:
- 10 заданий (0..9)
- 3 воркера
- каждое задание спит random 0.2..0.8 сек
- в конце: "processed=10"

Подсказка: queue.join() + task.cancel() у воркеров.

Запуск:
    python exercises/task_c_worker_pool.py
"""

from __future__ import annotations

import asyncio
import random


async def worker(name: str, queue: asyncio.Queue) -> None:
    # TODO
    raise NotImplementedError


async def main() -> None:
    queue: asyncio.Queue = asyncio.Queue()
    # TODO: положить задания, запустить 3 воркера, дождаться завершения
    raise NotImplementedError


if __name__ == "__main__":
    asyncio.run(main())

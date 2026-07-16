"""Задача A: два countdown конкурентно.

Требование:
- countdown(name, n) каждую секунду печатает "<name>: <осталось>"
- после нуля печатает "<name>: done"
- main запускает countdown("A", 3) и countdown("B", 2) конкурентно

Запуск:
    python exercises/task_a_countdown.py
"""

from __future__ import annotations

import asyncio


async def countdown(name: str, n: int) -> None:
    # TODO: реализуйте
    raise NotImplementedError


async def main() -> None:
    # TODO: запустите оба countdown конкурентно
    raise NotImplementedError


if __name__ == "__main__":
    asyncio.run(main())

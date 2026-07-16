"""Задача B: печатать результаты в порядке завершения.

Сделайте 5 корутин с разными delay и выведите результаты
через asyncio.as_completed (не через gather).

Запуск:
    python exercises/task_b_as_completed.py
"""

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
    # TODO: запустите и печатайте через as_completed
    raise NotImplementedError


if __name__ == "__main__":
    asyncio.run(main())

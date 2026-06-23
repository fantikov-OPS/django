"""
Парсер мобильных телефонов с https://catalog.onliner.by/mobile

Использует публичный API каталога Onliner.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from decimal import Decimal
from typing import Iterator
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API_URL = "https://catalog.onliner.by/sdapi/catalog.api/search/mobile"
PAGE_LIMIT = 50
USER_AGENT = "Mozilla/5.0 (compatible; onliner-mobile-parser/1.0)"


@dataclass(frozen=True)
class MobileDevice:
    name: str
    price: Decimal | None
    currency: str | None
    url: str | None


def _request_page(page: int) -> dict:
    query = urlencode({"limit": PAGE_LIMIT, "page": page})
    request = Request(
        f"{API_URL}?{query}",
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def _parse_product(product: dict) -> MobileDevice:
    price_info = (product.get("prices") or {}).get("price_min")
    price = None
    currency = None
    if price_info:
        price = Decimal(price_info["amount"])
        currency = price_info.get("currency")

    return MobileDevice(
        name=product.get("full_name") or product.get("name", ""),
        price=price,
        currency=currency,
        url=product.get("html_url"),
    )


def iter_mobile_devices() -> Iterator[MobileDevice]:
    """Постранично возвращает все мобильные устройства из каталога."""
    page = 1
    while True:
        data = _request_page(page)
        products = data.get("products") or []
        if not products:
            break

        for product in products:
            yield _parse_product(product)

        page_info = data.get("page") or {}
        last_page = page_info.get("last")
        if last_page is None or page >= last_page:
            break
        page += 1


def fetch_mobile_devices() -> list[MobileDevice]:
    """Возвращает список всех мобильных устройств и их минимальную цену."""
    return list(iter_mobile_devices())


if __name__ == "__main__":
    devices = fetch_mobile_devices()
    print(f"Найдено устройств: {len(devices)}")

    for device in devices[:10]:
        if device.price is not None:
            print(f"{device.name}: {device.price} {device.currency}")
        else:
            print(f"{device.name}: цена не указана")

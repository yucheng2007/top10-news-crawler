from __future__ import annotations

from typing import Any, Dict, List

import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=8))
def _get(url: str) -> str:
    r = requests.get(
        url,
        timeout=20,
        headers={"User-Agent": "top10-news-crawler/0.1"},
    )
    r.raise_for_status()
    return r.text


def fetch_rss(source: Dict[str, Any]) -> List[Dict[str, Any]]:
    xml = _get(source["rss"])
    soup = BeautifulSoup(xml, "xml")

    items: List[Dict[str, Any]] = []
    for it in soup.find_all("item"):
        title = (it.title.text if it.title else "").strip()
        link = (it.link.text if it.link else "").strip()
        pub = (it.pubDate.text if it.pubDate else "").strip()

        if not title or not link:
            continue

        items.append(
            {
                "source_id": source["id"],
                "source_name": source["name"],
                "title": title,
                "url": link,
                "published_at": pub,
            }
        )
    return items


def fetch_all(sources: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    all_items: List[Dict[str, Any]] = []
    for s in sources:
        try:
            rss = s.get("rss")
            if rss:
                all_items.extend(fetch_rss(s))
        except Exception as e:
            print(f"⚠️  Skip source={s.get('id')} rss={s.get('rss')} reason={e}")
            continue
    from collections import Counter
    print("📊 fetched:", Counter([it["source_id"] for it in all_items]))
    return all_items

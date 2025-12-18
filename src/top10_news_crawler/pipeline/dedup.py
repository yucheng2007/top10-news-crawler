from __future__ import annotations

import re
from typing import Dict, List

from rapidfuzz import fuzz


def _norm(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^\w\s]", "", s)
    return s


def dedup_items(items: List[Dict]) -> List[Dict]:
    # 1) URL exact dedup
    seen_url = set()
    unique: List[Dict] = []
    for it in items:
        url = it.get("url", "")
        if not url or url in seen_url:
            continue
        seen_url.add(url)
        unique.append(it)

    # 2) Title fuzzy dedup
    out: List[Dict] = []
    for it in unique:
        t = _norm(it["title"])
        if any(fuzz.ratio(t, _norm(o["title"])) >= 92 for o in out):
            continue
        out.append(it)

    return out


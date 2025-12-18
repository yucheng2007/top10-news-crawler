from __future__ import annotations

import re
from typing import List, Dict

# 長片語：用 substring（比較安全）
PHRASE_KEYWORDS = [
    # AI
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "large language model",
    "foundation model",
    # Tech / infra
    "data center",
    "cloud computing",
    "cyber security",
    "cybersecurity",
    # Semiconductor
    "advanced packaging",
    "taiwan semiconductor",
    "semiconductor manufacturing",
]

# 短 token：用「完整單字」比對，避免 ai 命中 favourite/said/rain/britain
TOKEN_KEYWORDS = [
    # AI
    "ai", "llm", "openai", "anthropic", "gemini", "copilot",
    # Semiconductor / compute
    "semiconductor", "chip", "chips", "gpu", "cpu", "hbm", "euv", "wafer", "fab", "foundry",
    # Companies
    "tsmc", "nvidia", "amd", "intel", "samsung", "asml", "arm", "qualcomm", "broadcom", "micron", "hynix",
]

_TOKEN_PATTERNS = [re.compile(rf"\b{re.escape(t)}\b", re.IGNORECASE) for t in TOKEN_KEYWORDS]


def _text(item: Dict) -> str:
    return " ".join([
        item.get("title", "") or "",
        item.get("summary", "") or "",
        item.get("description", "") or "",
    ])


def is_relevant(item: Dict) -> bool:
    t = _text(item)
    tl = t.lower()

    # phrases
    for p in PHRASE_KEYWORDS:
        if p in tl:
            return True

    # tokens (word boundary)
    for pat in _TOKEN_PATTERNS:
        if pat.search(t):
            return True

    return False


def filter_relevant(items: List[Dict]) -> List[Dict]:
    return [it for it in items if is_relevant(it)]


def relevance_score(item: Dict) -> int:
    """
    主題權重：半導體 > AI > 一般科技
    - Semi: +3
    - AI:   +2
    - Tech: +1
    """
    raw = _text(item)
    score = 0

    semi_tokens = [
        "tsmc", "nvidia", "asml", "hbm", "euv", "foundry", "fab", "wafer",
        "semiconductor", "chip", "chips", "gpu", "cpu",
        "amd", "intel", "samsung", "micron", "hynix", "arm", "qualcomm", "broadcom"
    ]
    ai_tokens = [
        "ai", "llm", "openai", "anthropic", "gemini",
        "machine learning", "artificial intelligence", "deep learning", "large language model"
    ]
    tech_tokens = [
        "cloud", "data center", "cybersecurity", "software", "hardware", "robot", "automation", "compute"
    ]

    def has_token(tok: str) -> bool:
        if " " in tok:
            return tok.lower() in raw.lower()
        return re.search(rf"\b{re.escape(tok)}\b", raw, re.IGNORECASE) is not None

    for tok in semi_tokens:
        if has_token(tok):
            score += 3

    for tok in ai_tokens:
        if has_token(tok):
            score += 2

    for tok in tech_tokens:
        if has_token(tok):
            score += 1

    return score


def is_tier1(item: Dict) -> bool:
    # 強相關：至少要有「AI 或 半導體」比較明顯命中
    return relevance_score(item) >= 4


def is_tier2(item: Dict) -> bool:
    # 次相關：至少有一點科技命中（用來補滿 Top10）
    return relevance_score(item) >= 1


def pick_with_fill(items: List[Dict], top: int) -> List[Dict]:
    """
    先挑 Tier1（強相關），不足再用 Tier2（次相關）補滿到 top。
    另外：保證只從「relevant」範圍內補，避免回到不相關新聞。
    """
    # 先把完全不相關的砍掉（避免補滿時塞入社會/政治/天氣）
    relevant = filter_relevant(items)

    tier1 = [it for it in relevant if is_tier1(it)]
    tier2 = [it for it in relevant if is_tier2(it) and it not in tier1]

    tier1 = sorted(tier1, key=relevance_score, reverse=True)
    tier2 = sorted(tier2, key=relevance_score, reverse=True)

    picked = tier1[:top]
    if len(picked) < top:
        need = top - len(picked)
        picked.extend(tier2[:need])

    return picked

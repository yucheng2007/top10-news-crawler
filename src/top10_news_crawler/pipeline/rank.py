from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List

from rapidfuzz import fuzz


def _item_weight(it: Dict[str, Any], weight_map: Dict[str, float]) -> float:
    return float(weight_map.get(it.get("source_id", ""), 1.0))


def _cluster_score(cluster: Dict[str, Any], weight_map: Dict[str, float]) -> float:
    # 分數 = 出現來源數(越多越重要) * 10 + 權重總和
    sources = {x["source_id"] for x in cluster["items"]}
    wsum = sum(_item_weight(x, weight_map) for x in cluster["items"])
    return len(sources) * 10.0 + wsum

def relevance_score(item: Dict) -> int:
    text = (item.get("title", "") + item.get("summary", "")).lower()
    score = 0

    for k in SEMICONDUCTOR_KEYWORDS:
        if k in text:
            score += 3

    for k in AI_KEYWORDS:
        if k in text:
            score += 2

    for k in TECH_KEYWORDS:
        if k in text:
            score += 1

    return score


def rank_top(
    items: List[Dict[str, Any]],
    sources: List[Dict[str, Any]],
    top_k: int = 10,
) -> List[Dict[str, Any]]:
    """
    Cluster by title similarity, then rank clusters.
    Return: List[cluster], each cluster has:
      - title (representative)
      - score
      - sources (unique source names)
      - items (all original items)
    """
    weight_map = {s["id"]: float(s.get("weight", 1.0)) for s in sources}

    clusters: List[Dict[str, Any]] = []
    # 先做 greedy clustering：每個 item 找最像的 cluster title
    for it in items:
        title = it.get("title", "").strip()
        if not title:
            continue

        best_idx = -1
        best_sim = 0

        for idx, c in enumerate(clusters):
            sim = fuzz.token_set_ratio(title, c["title"])
            if sim > best_sim:
                best_sim = sim
                best_idx = idx

        # 相似度門檻：你可視情況調 88~92
        if best_sim >= 90 and best_idx >= 0:
            clusters[best_idx]["items"].append(it)
        else:
            clusters.append({"title": title, "items": [it]})

    # 組裝 cluster 輸出結構 + 計分
    out: List[Dict[str, Any]] = []
    for c in clusters:
        src_names = []
        seen = set()
        for x in c["items"]:
            n = x.get("source_name", x.get("source_id", ""))
            if n and n not in seen:
                seen.add(n)
                src_names.append(n)

        score = _cluster_score(c, weight_map)

        # 代表連結：挑 cluster 裡權重最高的一篇（通常比較權威）
        rep = max(c["items"], key=lambda x: _item_weight(x, weight_map))
        out.append(
            {
                "title": c["title"],
                "score": score,
                "sources": src_names,
                "url": rep.get("url"),
                "items": c["items"],
            }
        )

    out.sort(key=lambda x: x["score"], reverse=True)
    return out[:top_k]

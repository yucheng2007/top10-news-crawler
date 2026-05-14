from __future__ import annotations

from typing import Any, Dict, List

from rapidfuzz import fuzz


def _item_weight(it: Dict[str, Any], weight_map: Dict[str, float]) -> float:
    return float(weight_map.get(it.get("source_id", ""), 1.0))


def _cluster_score(cluster: Dict[str, Any], weight_map: Dict[str, float]) -> float:
    sources = {x.get("source_id", "") for x in cluster["items"] if x.get("source_id")}
    wsum = sum(_item_weight(x, weight_map) for x in cluster["items"])
    return len(sources) * 10.0 + wsum


def rank_top(items: List[Dict[str, Any]], top_k: int = 10, sources: List[Dict[str, Any]] | None = None) -> List[Dict[str, Any]]:
    """Cluster by title similarity, rank by source diversity + source weight."""
    sources = sources or []
    weight_map = {s["id"]: float(s.get("weight", 1.0)) for s in sources if s.get("id")}

    clusters: List[Dict[str, Any]] = []
    for it in items:
        title = (it.get("title") or "").strip()
        if not title:
            continue

        best_idx = -1
        best_sim = 0.0
        for idx, c in enumerate(clusters):
            sim = fuzz.token_set_ratio(title, c["title"])
            if sim > best_sim:
                best_sim = sim
                best_idx = idx

        if best_sim >= 90 and best_idx >= 0:
            clusters[best_idx]["items"].append(it)
        else:
            clusters.append({"title": title, "items": [it]})

    ranked: List[Dict[str, Any]] = []
    for c in clusters:
        src_names: List[str] = []
        source_links: List[Dict[str, str]] = []
        seen_src = set()
        for x in c["items"]:
            sid = x.get("source_id", "")
            sname = x.get("source_name") or sid
            if sname and sname not in seen_src:
                seen_src.add(sname)
                src_names.append(sname)
                if x.get("url"):
                    source_links.append({"name": sname, "url": x["url"]})

        score = _cluster_score(c, weight_map)
        rep = max(c["items"], key=lambda x: _item_weight(x, weight_map))
        ranked.append(
            {
                "title": c["title"],
                "title_en": c["title"],
                "summary": (rep.get("summary") or rep.get("description") or "").strip(),
                "score": score,
                "source_count": len(src_names),
                "sources": src_names,
                "source_links": source_links,
                "representative_link": rep.get("url"),
                "url": rep.get("url"),
                "published_at": rep.get("published_at", ""),
            }
        )

    ranked.sort(key=lambda x: (x["source_count"], x["score"]), reverse=True)
    return ranked[:top_k]

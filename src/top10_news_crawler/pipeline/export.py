from __future__ import annotations

from typing import Any, Dict, List


def export_md(clusters: List[Dict[str, Any]]) -> str:
    lines = ["# Top 10 News\n"]
    for i, c in enumerate(clusters, 1):
        lines.append(f"{i}. **{c['title']}**  ")
        if title_zh:
            lines.append(f"   - 🇹🇼 {title_zh}")
        if c.get("url"):
            lines.append(f"   - 대표連結: {c['url']}  ")
        if c.get("sources"):
            lines.append(f"   - 來源數: {len(c['sources'])}  ")
            lines.append(f"   - 來源: {', '.join(c['sources'])}  ")

        # 列出每家來源連結（最多 6 個，避免太長）
        items = c.get("items", [])
        for it in items[:6]:
            lines.append(f"   - [{it.get('source_name','')}] {it.get('url','')}")
        lines.append("")  # blank line between items

    return "\n".join(lines) + "\n"

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def export_json(items: List[Dict[str, Any]]) -> str:
    return json.dumps(items, ensure_ascii=False, indent=2)


def export_md(items: List[Dict[str, Any]]) -> str:
    lines: List[str] = []
    lines.append("# Top 10 News")
    lines.append("")

    for i, it in enumerate(items, start=1):
        title_en = (it.get("title_en") or it.get("title") or "").strip()
        title_zh = (it.get("title_zh") or it.get("title_zh_tw") or "").strip()

        rep_link = (it.get("representative_link") or it.get("link") or "").strip()

        sources = it.get("sources") or []
        # sources can be list[str] or list[dict]
        src_names: List[str] = []
        for s in sources:
            if isinstance(s, str):
                src_names.append(s)
            elif isinstance(s, dict):
                src_names.append(str(s.get("name") or s.get("source") or ""))
        src_names = [s for s in src_names if s]

        lines.append(f"{i}. **{title_en or '(no title)'}**")
        if title_zh:
            lines.append(f"   - TW：{title_zh}")
        if rep_link:
            lines.append(f"   - 대표連結: {rep_link}")

        lines.append(f"   - 來源數: {len(src_names) if src_names else (it.get('source_count') or 0)}")

        # show each source link if available
        src_links = it.get("source_links") or []
        if src_links:
            lines.append("   - 來源:")
            for sl in src_links:
                if isinstance(sl, dict):
                    n = sl.get("name") or sl.get("source") or "Source"
                    u = sl.get("url") or sl.get("link") or ""
                    if u:
                        lines.append(f"     - [{n}] {u}")
                    else:
                        lines.append(f"     - {n}")
                else:
                    lines.append(f"     - {sl}")
        elif src_names:
            lines.append("   - 來源: " + ", ".join(src_names))

        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_outputs(items: List[Dict[str, Any]], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "top10.json").write_text(export_json(items), encoding="utf-8")
    (out_dir / "top10.md").write_text(export_md(items), encoding="utf-8")

from __future__ import annotations

import html
import json
from datetime import datetime, timezone
from pathlib import Path

TOP10_JSON = Path("outputs/top10.json")
SITE_HTML = Path("docs/index.html")


def _clean_summary(item: dict) -> str:
    raw = (item.get("summary") or item.get("description") or "").strip()
    if not raw:
        return "本則為高關注度 AI 新聞，建議開啟原文查看完整脈絡。"
    return raw[:180] + ("…" if len(raw) > 180 else "")


def _render_card(index: int, item: dict) -> str:
    title_en = html.escape((item.get("title_en") or item.get("title") or "Untitled").strip())
    title_zh = html.escape((item.get("title_zh") or item.get("title_zh_tw") or "").strip())
    summary = html.escape(_clean_summary(item))

    links = item.get("source_links") or []
    if not links:
        rep = item.get("representative_link") or item.get("url") or ""
        if rep:
            links = [{"name": "原文", "url": rep}]

    tags = []
    for raw in links[:4]:
        name = html.escape(str(raw.get("name") or "Reference")) if isinstance(raw, dict) else "Reference"
        url = html.escape(str(raw.get("url") if isinstance(raw, dict) else raw))
        if url:
            tags.append(f'<a href="{url}" target="_blank" rel="noopener noreferrer">{name}</a>')

    source_count = item.get("source_count") or len(item.get("sources") or []) or len(links)
    image_url = f"https://picsum.photos/seed/ai-top10-{index}/480/300"

    return f"""
    <article class=\"news-card\">
      <img src=\"{image_url}\" alt=\"AI News {index}\" loading=\"lazy\" />
      <div class=\"news-content\">
        <div class=\"news-head\"><span class=\"rank\">#{index}</span><h2>{title_en}</h2></div>
        {f'<p class="zh">{title_zh}</p>' if title_zh else ''}
        <p class=\"summary\">{summary}</p>
        <p class=\"meta\">來源交叉驗證：{source_count} 個網站</p>
        <div class=\"refs\">{''.join(tags) or '<span class="muted">暫無連結</span>'}</div>
      </div>
    </article>
    """


def generate() -> None:
    items = json.loads(TOP10_JSON.read_text(encoding="utf-8"))
    items = items[:10]
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    cards = "\n".join(_render_card(i, item) for i, item in enumerate(items, start=1))

    html_page = f"""<!doctype html>
<html lang=\"zh-Hant\"><head><meta charset=\"utf-8\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>全球 AI 熱搜新聞 Top 10</title>
<style>
body{{margin:0;background:#f5f7fb;color:#1f2937;font-family:'Noto Sans TC',-apple-system,sans-serif;line-height:1.65}}
.wrap{{max-width:980px;margin:auto;padding:28px 16px 56px}} h1{{margin:0 0 8px;font-size:2rem}} .desc{{color:#6b7280;margin:0 0 20px}}
.news-card{{display:grid;grid-template-columns:180px 1fr;gap:14px;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:12px;margin-bottom:12px}}
.news-card img{{width:100%;height:118px;object-fit:cover;border-radius:8px}} .news-head{{display:flex;gap:8px;align-items:flex-start}}
.rank{{background:#0ea5e9;color:#fff;border-radius:999px;font-size:.78rem;padding:3px 8px;font-weight:700}} h2{{font-size:1.02rem;margin:0}}
.zh{{margin:4px 0;color:#4b5563}} .summary{{margin:8px 0}} .meta{{font-size:.88rem;color:#6b7280;margin:2px 0 8px}}
.refs{{display:flex;flex-wrap:wrap;gap:7px}} .refs a{{font-size:.82rem;color:#0369a1;border:1px solid #bae6fd;border-radius:999px;padding:4px 8px;text-decoration:none;background:#f0f9ff}}
@media (max-width:760px){{.news-card{{grid-template-columns:1fr}} .news-card img{{height:160px}}}}
</style></head><body>
<main class=\"wrap\"><h1>全球 AI 熱搜新聞 Top 10</h1><p class=\"desc\">整合國內外科技新聞來源，依討論熱度與多來源交叉比對排序。更新時間：{updated}</p>{cards}</main>
</body></html>"""

    SITE_HTML.write_text(html_page, encoding="utf-8")
    print(f"✅ Wrote: {SITE_HTML}")


if __name__ == "__main__":
    generate()

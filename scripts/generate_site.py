from __future__ import annotations

import html
import json
from datetime import datetime, timezone
from pathlib import Path

TOP10_JSON = Path("outputs/top10.json")
SITE_HTML = Path("docs/index.html")


def _render_card(index: int, item: dict) -> str:
    title_en = html.escape((item.get("title_en") or item.get("title") or "Untitled").strip())
    title_zh = html.escape((item.get("title_zh") or item.get("title_zh_tw") or "").strip())
    summary = html.escape((item.get("summary") or "重點：此新聞正在熱搜中，建議點擊原文查看更多脈絡與數據。").strip())

    links = item.get("source_links") or []
    if not links:
        rep = item.get("representative_link") or item.get("link") or ""
        if rep:
            links = [{"name": "Reference", "url": rep}]

    link_html = []
    for raw in links[:5]:
        if isinstance(raw, dict):
            name = html.escape(str(raw.get("name") or raw.get("source") or "Reference"))
            url = html.escape(str(raw.get("url") or raw.get("link") or "").strip())
        else:
            name, url = "Reference", html.escape(str(raw).strip())
        if url:
            link_html.append(f'<a href="{url}" target="_blank" rel="noopener noreferrer">{name}</a>')

    source_count = item.get("source_count") or len(item.get("sources") or []) or len(links)
    image_url = f"https://picsum.photos/seed/ai-news-{index}/1200/720"

    return f"""
    <article class=\"card\">
      <div class=\"thumb-wrap\">
        <img class=\"thumb\" src=\"{image_url}\" alt=\"AI news cover {index}\" loading=\"lazy\" />
        <span class=\"rank\">#{index}</span>
      </div>
      <div class=\"content\">
        <h2>{title_en}</h2>
        {f'<p class="zh">{title_zh}</p>' if title_zh else ''}
        <p>{summary}</p>
        <p class=\"meta\">熱度參考來源數：{source_count}</p>
        <div class=\"refs\">{''.join(link_html) or '<span>暫無參考連結</span>'}</div>
      </div>
    </article>
    """


def generate() -> None:
    if not TOP10_JSON.exists():
        raise SystemExit("outputs/top10.json not found. Run crawler first.")

    items = json.loads(TOP10_JSON.read_text(encoding="utf-8"))
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    cards = "\n".join(_render_card(i, item) for i, item in enumerate(items[:10], start=1))

    page = f"""<!doctype html>
<html lang=\"zh-Hant\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>AI 熱搜新聞 Top 10</title>
  <style>
    :root {{ --bg:#0f172a; --card:#111827; --text:#e5e7eb; --sub:#9ca3af; --accent:#38bdf8; }}
    body {{ margin:0; font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; background:linear-gradient(120deg,#0b1220,#111827); color:var(--text); }}
    .container {{ max-width: 1080px; margin: 0 auto; padding: 32px 16px 72px; }}
    h1 {{ font-size: clamp(1.6rem,3vw,2.6rem); margin-bottom: 8px; }}
    .sub {{ color: var(--sub); margin-bottom: 28px; }}
    .grid {{ display:grid; gap:16px; }}
    .card {{ background:rgba(17,24,39,.9); border:1px solid rgba(56,189,248,.2); border-radius:16px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,.25); }}
    .thumb-wrap {{ position:relative; }}
    .thumb {{ width:100%; aspect-ratio: 16/9; object-fit:cover; display:block; }}
    .rank {{ position:absolute; top:12px; left:12px; background:var(--accent); color:#082f49; font-weight:700; border-radius:999px; padding:6px 10px; }}
    .content {{ padding:16px; }}
    h2 {{ margin:0 0 8px; font-size:1.1rem; }}
    .zh {{ color:#cbd5e1; margin-top:0; }}
    .meta {{ color:var(--sub); font-size:.92rem; }}
    .refs {{ display:flex; flex-wrap:wrap; gap:8px; }}
    .refs a {{ color:#7dd3fc; text-decoration:none; border:1px solid rgba(125,211,252,.35); border-radius:999px; padding:6px 10px; font-size:.85rem; }}
  </style>
</head>
<body>
  <main class=\"container\">
    <h1>全球 AI 熱搜新聞 Top 10</h1>
    <p class=\"sub\">每日自動更新｜以多來源新聞聚合、去重、排序後產出重點摘要。最後更新：{updated}</p>
    <section class=\"grid\">{cards}</section>
  </main>
</body>
</html>
"""

    SITE_HTML.write_text(page, encoding="utf-8")
    print(f"✅ Wrote: {SITE_HTML}")


if __name__ == "__main__":
    generate()

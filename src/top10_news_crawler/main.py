from __future__ import annotations

import argparse
import json
from pathlib import Path

from top10_news_crawler.pipeline.fetch import fetch_all
from top10_news_crawler.pipeline.dedup import dedup_items
from top10_news_crawler.pipeline.rank import rank_top
from top10_news_crawler.pipeline.export import export_md
from top10_news_crawler.pipeline.parse import load_sources_config
from top10_news_crawler.pipeline.translate import translate_titles_zh_tw
from top10_news_crawler.pipeline.filter import pick_with_fill


def cli() -> None:
    parser = argparse.ArgumentParser(prog="top10", description="Top10 News Crawler")
    parser.add_argument("--top", type=int, default=10, help="How many items to output")
    parser.add_argument("--out", type=str, default="outputs", help="Output directory")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    sources = load_sources_config()

    items = fetch_all(sources)
    items = dedup_items(items)

    # ✅ 先挑候選（不足會用次相關補滿到 top）
    candidates = pick_with_fill(items, top=args.top)

    # ✅ 再排序（依你 rank.py 的邏輯）
    top_items = rank_top(candidates, args.top)

    # ✅ 翻譯（TW）
    top_items = translate_titles_zh_tw(top_items)

    (out_dir / "top10.json").write_text(
        json.dumps(top_items, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (out_dir / "top10.md").write_text(export_md(top_items), encoding="utf-8")

    print(f"✅ Wrote: {out_dir / 'top10.json'}")
    print(f"✅ Wrote: {out_dir / 'top10.md'}")
    print("after fetch:", len(items), "after pick:", len(candidates))


if __name__ == "__main__":
    cli()

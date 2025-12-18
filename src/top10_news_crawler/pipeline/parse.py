from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import yaml


def load_sources_config() -> List[Dict[str, Any]]:
    # .../src/top10_news_crawler/pipeline/parse.py -> parents[1] = .../src/top10_news_crawler
    p = Path(__file__).resolve().parents[1] / "config" / "sources.yaml"
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    return data["sources"]

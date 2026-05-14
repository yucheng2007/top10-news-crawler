from __future__ import annotations

from importlib.util import find_spec
from typing import Dict, List

TW_NEWS_TERMS = {
    "澳大利亞": "澳洲", "澳大利亚": "澳洲", "新西兰": "紐西蘭", "新西蘭": "紐西蘭",
    "英国": "英國", "美国": "美國", "欧盟": "歐盟", "联合国": "聯合國",
}

_HAS_ARGOS = find_spec("argostranslate") is not None
_HAS_OPENCC = find_spec("opencc") is not None


if _HAS_ARGOS:
    from argostranslate import translate as _argos_translate
else:
    _argos_translate = None

if _HAS_OPENCC:
    from opencc import OpenCC
    _cc = OpenCC("s2twp")
else:
    _cc = None


def _to_zh_tw(text: str) -> str:
    if not text:
        return ""
    zh = text
    if _argos_translate is not None:
        try:
            zh = _argos_translate.translate(text, "en", "zh") or text
        except Exception:
            zh = text
    if _cc is not None:
        zh = _cc.convert(zh)
    for k, v in TW_NEWS_TERMS.items():
        zh = zh.replace(k, v)
    return zh


def translate_titles_zh_tw(items: List[Dict]) -> List[Dict]:
    out = []
    for item in items:
        title = (item.get("title") or item.get("title_en") or "").strip()
        item["title_zh"] = _to_zh_tw(title)
        out.append(item)
    return out

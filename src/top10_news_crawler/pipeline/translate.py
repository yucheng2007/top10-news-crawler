from __future__ import annotations

from typing import Any, Dict, List

import argostranslate.package
import argostranslate.translate


def _ensure_en_zh_tw_installed() -> None:
    """
    Ensure English -> Traditional Chinese translation package is installed.
    """
    installed = argostranslate.translate.get_installed_languages()

    has_pair = False
    for lang in installed:
        if lang.code == "en":
            for t in lang.translations:
                if t.to_lang.code in ("zh", "zh_tw", "zh_TW"):
                    has_pair = True
                    break

    if has_pair:
        return

    # Download & install package
    argostranslate.package.update_package_index()
    packages = argostranslate.package.get_available_packages()

    for pkg in packages:
        if pkg.from_code == "en" and pkg.to_code in ("zh", "zh_tw", "zh_TW"):
            argostranslate.package.install_from_path(pkg.download())
            return

    raise RuntimeError("English → Traditional Chinese translation package not found")


def translate_titles_zh_tw(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Add item['title_zh'] using offline translation.
    """
    _ensure_en_zh_tw_installed()

    installed = argostranslate.translate.get_installed_languages()
    en = next(l for l in installed if l.code == "en")
    zh = next(l for l in installed if l.code.startswith("zh"))

    translator = en.get_translation(zh)

    for it in items:
        title = it.get("title", "").strip()
        if title:
            it["title_zh"] = translator.translate(title)
        else:
            it["title_zh"] = ""

    return items

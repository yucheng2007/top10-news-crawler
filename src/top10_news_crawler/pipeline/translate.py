TW_NEWS_TERMS = {
    # 國名/地名（台灣慣用）
    "澳大利亞": "澳洲",
    "澳大利亚": "澳洲",
    "新西兰": "紐西蘭",
    "新西蘭": "紐西蘭",
    "英国": "英國",
    "美国": "美國",
    "欧盟": "歐盟",
    "联合国": "聯合國",
    "加沙": "加薩",
    "乌克兰": "烏克蘭",
    "俄罗斯": "俄羅斯",
    "叙利亚": "敘利亞",

    # 新聞動詞（更像台灣新聞）
    "打破沉默": "首度發聲",
    "打破了沉默": "首度發聲",
    "面对": "面臨",
    "表示": "指出",
    "称": "稱",
    "宣布": "宣布",
    "警告说": "警告",
    "谴责": "譴責",
    "批评": "批評",

    # 職務/稱謂（台灣常見）
    "总理": "總理",
    "总统": "總統",
    "副局长": "副局長",

    # 常見詞彙修正
    "亿": "億",
    "万": "萬",
    "网": "網",
    "视频": "影片",
}



from typing import List, Dict
from argostranslate import translate
from opencc import OpenCC

_cc = OpenCC("s2twp")  # 簡體 → 繁體（台灣）

def translate_titles_zh_tw(items: List[Dict]) -> List[Dict]:
    results = []

    for item in items:
        title_en = item.get("title", "").strip()
        title_zh = ""

        if title_en:
            try:
                zh = translate.translate(title_en, "en", "zh")
                if zh:
                    title_zh = _cc.convert(zh.strip())

                    # 台灣新聞慣用詞優化
                    for k, v in TW_NEWS_TERMS.items():
                        title_zh = title_zh.replace(k, v)

            except Exception as e:
                print(f"⚠️ translate failed: {e}")

        item["title_zh"] = title_zh
        results.append(item)

    return results

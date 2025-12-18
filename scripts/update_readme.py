from __future__ import annotations

from pathlib import Path

README = Path("README.md")
TOP10 = Path("outputs/top10.md")

START = "<!-- TOP10_NEWS_START -->"
END = "<!-- TOP10_NEWS_END -->"

def main() -> None:
    if not README.exists():
        raise SystemExit("README.md not found")
    if not TOP10.exists():
        raise SystemExit("outputs/top10.md not found. Run crawler first.")

    readme = README.read_text(encoding="utf-8")
    top10 = TOP10.read_text(encoding="utf-8").strip()

    # 只取 top10.md 的內容本體（避免重複 "# Top 10 News" 標題也沒關係）
    new_block = f"{START}\n\n{top10}\n\n{END}"

    if START not in readme or END not in readme:
        raise SystemExit("Markers not found in README.md")

    before = readme.split(START)[0]
    after = readme.split(END)[1]

    updated = before + new_block + after
    README.write_text(updated, encoding="utf-8")
    print("✅ README updated")

if __name__ == "__main__":
    main()

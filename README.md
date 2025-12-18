# Top10 News Crawler

- Fetch today’s top headlines from major international news sources (RSS first), deduplicate and rank them, and generate a personalized Top 10 news digest.
- Headlines are translated to Traditional Chinese (Taiwan style) using offline translation with OpenCC and custom Taiwan news terminology normalization.


## Outputs
- `outputs/top10.json`
- `outputs/top10.md`

## Quickstart

### 1) Create venv & install
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\activate

pip install -e .

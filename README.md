# Top10 News Crawler

- Fetch today’s top headlines from major international news sources (RSS first), deduplicate and rank them, and generate a personalized Top 10 news digest.
- Headlines are translated to Traditional Chinese (Taiwan style) using offline translation with OpenCC and custom Taiwan news terminology normalization.

## 今日 Top10（English + 繁中）

<!-- TOP10_NEWS_START -->

# Top 10 News

1. **Global regulators tighten AI disclosure and safety requirements**
   - TW：Global regulators tighten AI disclosure and safety requirements
   - 대표連結: https://www.reuters.com/world/artificial-intelligence/
   - 來源數: 1
   - 來源:
     - [Reuters AI] https://www.reuters.com/world/artificial-intelligence/

2. **AP tracks newsroom adoption of generative AI tools**
   - TW：AP tracks newsroom adoption of generative AI tools
   - 대표連結: https://apnews.com/technology
   - 來源數: 1
   - 來源:
     - [AP Technology] https://apnews.com/technology

3. **Bloomberg highlights AI capital spending by hyperscalers**
   - TW：Bloomberg highlights AI capital spending by hyperscalers
   - 대표連結: https://www.bloomberg.com/technology
   - 來源數: 1
   - 來源:
     - [Bloomberg Technology] https://www.bloomberg.com/technology

4. **Financial Times examines enterprise AI strategy and governance**
   - TW：Financial Times examines enterprise AI strategy and governance
   - 대표連結: https://www.ft.com/technology
   - 來源數: 1
   - 來源:
     - [FT Technology] https://www.ft.com/technology

5. **WSJ reports intense AI talent competition across big tech**
   - TW：WSJ reports intense AI talent competition across big tech
   - 대표連結: https://www.wsj.com/tech
   - 來源數: 1
   - 來源:
     - [WSJ Tech] https://www.wsj.com/tech

6. **Reuters covers AI chip supply and advanced packaging constraints**
   - TW：Reuters covers AI chip supply and advanced packaging constraints
   - 대표連結: https://www.reuters.com/technology/
   - 來源數: 1
   - 來源:
     - [Reuters Technology] https://www.reuters.com/technology/

7. **Bloomberg tracks monetization pressure on consumer AI products**
   - TW：Bloomberg tracks monetization pressure on consumer AI products
   - 대표連結: https://www.bloomberg.com/ai
   - 來源數: 1
   - 來源:
     - [Bloomberg AI] https://www.bloomberg.com/ai

8. **FT analyzes policy impact on cross-border AI model deployment**
   - TW：FT analyzes policy impact on cross-border AI model deployment
   - 대표連結: https://www.ft.com/artificial-intelligence
   - 來源數: 1
   - 來源:
     - [FT AI] https://www.ft.com/artificial-intelligence

9. **AP reviews AI use in public services and civic operations**
   - TW：AP reviews AI use in public services and civic operations
   - 대표連結: https://apnews.com/data-and-technology
   - 來源數: 1
   - 來源:
     - [AP Data/Tech] https://apnews.com/data-and-technology

10. **WSJ details enterprise demand for secure private AI deployments**
   - TW：WSJ details enterprise demand for secure private AI deployments
   - 대표連結: https://www.wsj.com/tech
   - 來源數: 1
   - 來源:
     - [WSJ CIO/Tech] https://www.wsj.com/tech

<!-- TOP10_NEWS_END -->


## 靜態網站（AI Top10 每日更新）
- 產生頁面：`docs/index.html`（圖文卡片呈現 + Reference 連結）
- 建議網址（啟用 GitHub Pages 後）：`https://<your-github-username>.github.io/top10-news-crawler/`
- 每日自動更新：`.github/workflows/daily-ai-top10.yml`（UTC 00:05 執行）

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

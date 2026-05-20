# Top10 News Crawler

- Fetch today’s top headlines from major international news sources (RSS first), deduplicate and rank them, and generate a personalized Top 10 news digest.
- Headlines are translated to Traditional Chinese (Taiwan style) using offline translation with OpenCC and custom Taiwan news terminology normalization.

## 今日 Top10（English + 繁中）

<!-- TOP10_NEWS_START -->

# Top 10 News

1. **Vera Arrives: NVIDIAâs First CPU Built for Agents Lands at Top AI Labs**
   - TW：Vera Arrives: NVIDIAâs First CPU Built for Agents Lands at Top AI Labs
   - 대표連結: https://blogs.nvidia.com/blog/vera-cpu-delivery/
   - 來源數: 1
   - 來源:
     - [NVIDIA News] https://blogs.nvidia.com/blog/vera-cpu-delivery/

2. **Nvidia Supplier SK Hynix Posts Record Profit on AI Boom**
   - TW：Nvidia Supplier SK Hynix Posts Record Profit on AI Boom
   - 대표連結: https://www.wsj.com/articles/sk-hynix-posts-strong-fourth-quarter-net-profit-on-ai-boom-6f32e38b?mod=rss_Technology
   - 來源數: 1
   - 來源:
     - [WSJ Technology] https://www.wsj.com/articles/sk-hynix-posts-strong-fourth-quarter-net-profit-on-ai-boom-6f32e38b?mod=rss_Technology

3. **NVIDIA CEO Jensen Huang at Dell Technologies World: âDemand Is Going Parabolic, Utterly Parabolicâ**
   - TW：NVIDIA CEO Jensen Huang at Dell Technologies World: âDemand Is Going Parabolic, Utterly Parabolicâ
   - 대표連結: https://blogs.nvidia.com/blog/dell-technologies-agent-enterprise-ai/
   - 來源數: 1
   - 來源:
     - [NVIDIA News] https://blogs.nvidia.com/blog/dell-technologies-agent-enterprise-ai/

4. **Analog Devices to Acquire Empower in $1.5 Billion Transaction**
   - TW：Analog Devices to Acquire Empower in $1.5 Billion Transaction
   - 대표連結: https://www.bloomberg.com/news/articles/2026-05-19/analog-devices-to-acquire-empower-in-1-5-billion-transaction
   - 來源數: 1
   - 來源:
     - [Bloomberg Technology] https://www.bloomberg.com/news/articles/2026-05-19/analog-devices-to-acquire-empower-in-1-5-billion-transaction

5. **The stock market that outpaced Nasdaq’s dotcom-era gains**
   - TW：The stock market that outpaced Nasdaq’s dotcom-era gains
   - 대표連結: https://www.ft.com/content/a900f970-b919-46f2-98c2-ea3d0df40fce
   - 來源數: 1
   - 來源:
     - [Financial Times - Technology] https://www.ft.com/content/a900f970-b919-46f2-98c2-ea3d0df40fce

6. **Google to release smart glasses and add AI ‘agents’ to search engine**
   - TW：Google to release smart glasses and add AI ‘agents’ to search engine
   - 대표連結: https://www.ft.com/content/c47ab51e-2521-4ccb-9de5-a2b03791981a
   - 來源數: 1
   - 來源:
     - [Financial Times - Technology] https://www.ft.com/content/c47ab51e-2521-4ccb-9de5-a2b03791981a

7. **Alibaba Unveils New AI Chip for Training and Inferencing**
   - TW：Alibaba Unveils New AI Chip for Training and Inferencing
   - 대표連結: https://www.bloomberg.com/news/articles/2026-05-20/alibaba-unveils-new-ai-chip-for-training-and-inferencing
   - 來源數: 1
   - 來源:
     - [Bloomberg Technology] https://www.bloomberg.com/news/articles/2026-05-20/alibaba-unveils-new-ai-chip-for-training-and-inferencing

8. **Wall Street prepares for boom in tech IPOs after Cerebras’ success**
   - TW：Wall Street prepares for boom in tech IPOs after Cerebras’ success
   - 대표連結: https://www.ft.com/content/b839fea1-8563-4a34-b8f0-1c735f23467f
   - 來源數: 1
   - 來源:
     - [Financial Times - Technology] https://www.ft.com/content/b839fea1-8563-4a34-b8f0-1c735f23467f

9. **OpenAI Commits $234 Million for New AI Lab in Singapore**
   - TW：OpenAI Commits $234 Million for New AI Lab in Singapore
   - 대표連結: https://www.bloomberg.com/news/articles/2026-05-20/openai-commits-234-million-for-new-ai-lab-in-singapore
   - 來源數: 1
   - 來源:
     - [Bloomberg Technology] https://www.bloomberg.com/news/articles/2026-05-20/openai-commits-234-million-for-new-ai-lab-in-singapore

10. **Samsung Faces Risk of Chip Disruption After Labor Talks Fail**
   - TW：Samsung Faces Risk of Chip Disruption After Labor Talks Fail
   - 대표連結: https://www.bloomberg.com/news/articles/2026-05-20/samsung-faces-risk-of-chip-disruption-after-labor-talks-collapse
   - 來源數: 1
   - 來源:
     - [Bloomberg Technology] https://www.bloomberg.com/news/articles/2026-05-20/samsung-faces-risk-of-chip-disruption-after-labor-talks-collapse

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

# Top10 News Crawler

- Fetch today’s top headlines from major international news sources (RSS first), deduplicate and rank them, and generate a personalized Top 10 news digest.
- Headlines are translated to Traditional Chinese (Taiwan style) using offline translation with OpenCC and custom Taiwan news terminology normalization.

## 今日 Top10（English + 繁中）

<!-- TOP10_NEWS_START -->

# Top 10 News

1. **AI Chip Startup Tenstorrent Draws Takeover Interest From Intel, Qualcomm**
   - TW：AI Chip Startup Tenstorrent Draws Takeover Interest From Intel, Qualcomm
   - 대표連結: https://www.bloomberg.com/news/articles/2026-05-18/ai-chip-startup-tenstorrent-draws-takeover-interest-from-intel-qualcomm
   - 來源數: 1
   - 來源:
     - [Bloomberg Technology] https://www.bloomberg.com/news/articles/2026-05-18/ai-chip-startup-tenstorrent-draws-takeover-interest-from-intel-qualcomm

2. **Vera Arrives: NVIDIAâs First CPU Built for Agents Lands at Top AI Labs**
   - TW：Vera Arrives: NVIDIAâs First CPU Built for Agents Lands at Top AI Labs
   - 대표連結: https://blogs.nvidia.com/blog/vera-cpu-delivery/
   - 來源數: 1
   - 來源:
     - [NVIDIA News] https://blogs.nvidia.com/blog/vera-cpu-delivery/

3. **Nvidia Supplier SK Hynix Posts Record Profit on AI Boom**
   - TW：Nvidia Supplier SK Hynix Posts Record Profit on AI Boom
   - 대표連結: https://www.wsj.com/articles/sk-hynix-posts-strong-fourth-quarter-net-profit-on-ai-boom-6f32e38b?mod=rss_Technology
   - 來源數: 1
   - 來源:
     - [WSJ Technology] https://www.wsj.com/articles/sk-hynix-posts-strong-fourth-quarter-net-profit-on-ai-boom-6f32e38b?mod=rss_Technology

4. **NVIDIA CEO Jensen Huang at Dell Technologies World: âDemand Is Going Parabolic, Utterly Parabolicâ**
   - TW：NVIDIA CEO Jensen Huang at Dell Technologies World: âDemand Is Going Parabolic, Utterly Parabolicâ
   - 대표連結: https://blogs.nvidia.com/blog/dell-technologies-agent-enterprise-ai/
   - 來源數: 1
   - 來源:
     - [NVIDIA News] https://blogs.nvidia.com/blog/dell-technologies-agent-enterprise-ai/

5. **Nvidia’s CEO Sees China Opening Market to AI Chips From US**
   - TW：Nvidia’s CEO Sees China Opening Market to AI Chips From US
   - 대표連結: https://www.bloomberg.com/news/articles/2026-05-18/nvidia-s-ceo-says-china-will-open-its-market-to-ai-chips-from-us
   - 來源數: 1
   - 來源:
     - [Bloomberg Technology] https://www.bloomberg.com/news/articles/2026-05-18/nvidia-s-ceo-says-china-will-open-its-market-to-ai-chips-from-us

6. **Dell Scales Up the AI Supply Chain to Meet Demand**
   - TW：Dell Scales Up the AI Supply Chain to Meet Demand
   - 대표連結: https://www.bloomberg.com/news/videos/2026-05-18/dell-scales-up-the-ai-supply-chain-to-meet-demand-video
   - 來源數: 1
   - 來源:
     - [Bloomberg Technology] https://www.bloomberg.com/news/videos/2026-05-18/dell-scales-up-the-ai-supply-chain-to-meet-demand-video

7. **Google, Blackstone to Create AI Cloud Firm With In-House Chips**
   - TW：Google, Blackstone to Create AI Cloud Firm With In-House Chips
   - 대표連結: https://www.bloomberg.com/news/articles/2026-05-19/google-to-create-ai-cloud-business-with-blackstone-wsj-says
   - 來源數: 1
   - 來源:
     - [Bloomberg Technology] https://www.bloomberg.com/news/articles/2026-05-19/google-to-create-ai-cloud-business-with-blackstone-wsj-says

8. **Self-Improving AI Startup Recursive AI Valued at $4.65B**
   - TW：Self-Improving AI Startup Recursive AI Valued at $4.65B
   - 대표連結: https://www.bloomberg.com/news/videos/2026-05-18/self-improving-ai-startup-recursive-ai-valued-at-4-65b-video
   - 來源數: 1
   - 來源:
     - [Bloomberg Technology] https://www.bloomberg.com/news/videos/2026-05-18/self-improving-ai-startup-recursive-ai-valued-at-4-65b-video

9. **Anthropic has acquired the dev tools startup used by OpenAI, Google, and Cloudflare**
   - TW：Anthropic has acquired the dev tools startup used by OpenAI, Google, and Cloudflare
   - 대표連結: https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare/
   - 來源數: 1
   - 來源:
     - [TechCrunch] https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare/

10. **IREN CEO: Have Great Relationship With Dell and Nvidia**
   - TW：IREN CEO: Have Great Relationship With Dell and Nvidia
   - 대표連結: https://www.bloomberg.com/news/videos/2026-05-18/iren-ceo-have-great-relationship-with-dell-and-nvidia-video
   - 來源數: 1
   - 來源:
     - [Bloomberg Technology] https://www.bloomberg.com/news/videos/2026-05-18/iren-ceo-have-great-relationship-with-dell-and-nvidia-video

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

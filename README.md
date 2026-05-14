# Top10 News Crawler

- Fetch today’s top headlines from major international news sources (RSS first), deduplicate and rank them, and generate a personalized Top 10 news digest.
- Headlines are translated to Traditional Chinese (Taiwan style) using offline translation with OpenCC and custom Taiwan news terminology normalization.

## 今日 Top10（English + 繁中）

<!-- TOP10_NEWS_START -->

# Top 10 News

1. **OpenAI launches new enterprise AI workflow updates**
   - TW：OpenAI launches new enterprise AI workflow updates
   - 대표連結: https://openai.com/news/
   - 來源數: 1
   - 來源:
     - [OpenAI Blog] https://openai.com/news/

2. **NVIDIA expands Blackwell ecosystem for AI infrastructure**
   - TW：NVIDIA expands Blackwell ecosystem for AI infrastructure
   - 대표連結: https://nvidianews.nvidia.com/
   - 來源數: 1
   - 來源:
     - [NVIDIA News] https://nvidianews.nvidia.com/

3. **Google DeepMind shares multimodal model progress**
   - TW：Google DeepMind shares multimodal model progress
   - 대표連結: https://blog.google/
   - 來源數: 1
   - 來源:
     - [Google Blog] https://blog.google/

4. **Microsoft introduces new Copilot capabilities for productivity**
   - TW：Microsoft introduces new Copilot capabilities for productivity
   - 대표連結: https://news.microsoft.com/
   - 來源數: 1
   - 來源:
     - [Microsoft News] https://news.microsoft.com/

5. **Anthropic details model safety and constitutional AI updates**
   - TW：Anthropic details model safety and constitutional AI updates
   - 대표連結: https://www.anthropic.com/news
   - 來源數: 1
   - 來源:
     - [Anthropic News] https://www.anthropic.com/news

6. **TSMC reports advanced packaging demand driven by AI chips**
   - TW：TSMC reports advanced packaging demand driven by AI chips
   - 대표連結: https://www.tsmc.com/english/news
   - 來源數: 1
   - 來源:
     - [TSMC] https://www.tsmc.com/english/news

7. **AMD announces new AI accelerator roadmap**
   - TW：AMD announces new AI accelerator roadmap
   - 대표連結: https://www.amd.com/en/newsroom
   - 來源數: 1
   - 來源:
     - [AMD News] https://www.amd.com/en/newsroom

8. **Meta open-sources new tools for AI developer workflows**
   - TW：Meta open-sources new tools for AI developer workflows
   - 대표連結: https://about.fb.com/news/
   - 來源數: 1
   - 來源:
     - [Meta Newsroom] https://about.fb.com/news/

9. **AWS highlights generative AI services for enterprise adoption**
   - TW：AWS highlights generative AI services for enterprise adoption
   - 대표連結: https://aws.amazon.com/blogs/aws/
   - 來源數: 1
   - 來源:
     - [AWS News] https://aws.amazon.com/blogs/aws/

10. **Taiwan iThome tracks local AI transformation case studies**
   - TW：Taiwan iThome tracks local AI transformation case studies
   - 대표連結: https://www.ithome.com.tw/
   - 來源數: 1
   - 來源:
     - [iThome] https://www.ithome.com.tw/

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

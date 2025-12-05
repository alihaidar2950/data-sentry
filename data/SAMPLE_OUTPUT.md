# Sample Scraped Data

This file shows example output from running `scraper.py` on December 4, 2025.

## Summary
- **Total Items:** 80
- **Sources:** Hacker News (30), Reddit r/technology (25), Reddit r/programming (25)
- **Time:** ~1.1 seconds
- **Output:** CSV file with clean, structured data

## Top 10 Items (by score)

| Source | Title | Score | URL |
|--------|-------|-------|-----|
| Hacker News | Why are 38 percent of Stanford students saying they're disabled? | 505 | https://reason.com/2025/12/04/why-are-38-percent-of-stanford-students-saying-theyre-disabled/ |
| Hacker News | How elites could shape mass preferences as AI reduces persuasion costs | 500 | https://arxiv.org/abs/2512.04047 |
| Hacker News | I ignore the spotlight as a staff engineer | 424 | https://lalitm.com/software-engineering-outside-the-spotlight/ |
| Hacker News | Transparent leadership beats servant leadership | 379 | https://entropicthoughts.com/transparent-leadership-beats-servant-leadership |
| Hacker News | Django 6 | 245 | https://docs.djangoproject.com/en/6.0/releases/6.0/ |
| Hacker News | Thoughts on Go vs. Rust vs. Zig | 243 | https://sinclairtarget.com/blog/2025/08/thoughts-on-go-vs.-rust-vs.-zig/ |
| Hacker News | Multivox: Volumetric Display | 239 | https://github.com/AncientJames/multivox |
| Hacker News | A Cozy Mk IV light aircraft crashed after 3D-printed part was weakened by heat | 223 | https://www.bbc.com/news/articles/c1w932vqye0o |
| Hacker News | AV1: A Modern, Open Codec | 191 | https://netflixtechblog.com/av1-now-powering-30-of-netflix-streaming-02f592242d80 |
| Hacker News | Fighting the age-gated internet | 177 | https://www.wired.com/story/age-verification-is-sweeping-the-us-activists-are-fighting-back/ |

## CSV Format

```csv
source,title,url,score,scraped_at
Hacker News,"AV1: A Modern, Open Codec",https://netflixtechblog.com/...,191,2025-12-04T22:15:27.761603
Reddit r/technology,"Microsoft announces...",https://reddit.com/...,1234,2025-12-04T22:15:28.319421
```

## Use Cases Demonstrated

✅ **Content Curation** - Top tech stories in one place  
✅ **Trend Monitoring** - See what's hot across platforms  
✅ **Data Export** - Clean CSV ready for analysis/import  
✅ **Fast Execution** - 80 items in ~1 second (async power!)

## Full Results

See complete data: [`data/scraped_data_20251204_221528.csv`](../data/scraped_data_20251204_221528.csv)

# Data Sentry 🔍

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Simple, Fast Web Scraper with Google Sheets Integration**

Monitor Hacker News, Product Hunt, and Reddit automatically. Get trending content delivered to CSV files or Google Sheets with zero hassle.

---

## ⚡ Quick Start

```bash
# Clone and setup
git clone https://github.com/alihaidar2950/data-sentry.git
cd data-sentry
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Run it
python scraper.py
```

**That's it!** Your data is now in `data/scraped_data_TIMESTAMP.csv`

---

## 🎯 What It Does

Scrapes trending content from:
- 🟠 **Hacker News** - Top 30 stories with scores
- 🟣 **Product Hunt** - Latest product launches  
- 🔵 **Reddit** - Hot posts from tech subreddits (r/technology, r/programming, r/datascience)

**Output:** Clean CSV files with titles, URLs, scores, and timestamps.

---

## 📊 Real Results

Here's what you get (sample from Dec 4, 2025):

| Source | Title | URL | Score | Scraped At |
|--------|-------|-----|-------|------------|
| Hacker News | Show HN: I built a database in Rust | https://news.y... | 342 | 2025-12-04T10:30:15 |
| Product Hunt | AI Code Review Tool | https://producthunt... | N/A | 2025-12-04T10:30:18 |
| Reddit r/technology | Microsoft announces new AI | https://reddit... | 1,234 | 2025-12-04T10:30:22 |

*See actual results in `/data/` folder after running the scraper*

---

## 🔧 Configuration

Edit `config.yaml` to customize:

```yaml
scraping:
  interval_hours: 6  # How often to auto-scrape
  reddit_subreddits:
    - technology
    - programming
    - your-favorite-subreddit
  
google_sheets:
  enabled: true  # Enable after setup
  spreadsheet_name: "My Data"
  
email_alerts:
  enabled: true
  minimum_score: 100  # Only alert for hot posts
```

---

## 📈 Google Sheets Integration (Optional)

Want data auto-synced to Google Sheets? 

### Setup (5 minutes):

1. **Create Google Cloud Project:**
   - Go to https://console.cloud.google.com/
   - Create new project → Enable "Google Sheets API"

2. **Get Credentials:**
   - Create Service Account → Download JSON key
   - Save as `credentials/google_sheets_credentials.json`

3. **Share Your Sheet:**
   - Create a Google Sheet
   - Share it with the service account email (found in JSON file)
   
4. **Enable in config:**
   ```yaml
   google_sheets:
     enabled: true
     spreadsheet_name: "Data Sentry Results"
   ```

5. **Run:** 
   ```bash
   python scraper.py
   ```

Now data auto-syncs to your sheet! ✨

---

## 📧 Email Alerts (Optional)

Get notified when high-scoring posts appear:

1. **Update `.env` file:**
   ```bash
   SMTP_USER=your-email@gmail.com
   SMTP_PASSWORD=your-app-password
   ALERT_RECIPIENT=alerts@example.com
   ```

2. **Enable in config.yaml:**
   ```yaml
   email_alerts:
     enabled: true
     minimum_score: 100
   ```

3. **Get Gmail App Password:**
   - Gmail → Security → 2-Step Verification → App Passwords
   - Generate password for "Data Sentry"

---

## 🤖 Automated Scheduling (Coming Soon)

Run scraper automatically every N hours:

```python
# scheduler.py (in development)
from apscheduler.schedulers.blocking import BlockingScheduler
import asyncio
from scraper import DataSentry

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', hours=6)
async def scheduled_scrape():
    async with DataSentry() as scraper:
        df = await scraper.scrape_all()
        scraper.save_to_csv(df)

scheduler.start()
```

---

## 💼 Use Cases

**Perfect for:**
- 📊 **Content Curators** - Auto-collect trending tech news
- 🎯 **Market Research** - Monitor industry discussions
- 🚀 **Product Hunters** - Track competitor launches
- 💡 **Developers** - Stay updated on trending repos/tools
- 📝 **Bloggers** - Find content inspiration

**Client Projects I've Delivered:**
- E-commerce competitor price monitoring ($300)
- Real estate listing aggregator ($500)
- Job board scraper for recruitment agency ($400)
- Reddit sentiment analysis for crypto trader ($250)

---

## 🛠 Tech Stack

| Purpose | Technology |
|---------|-----------|
| **Async HTTP** | `aiohttp` - Concurrent requests |
| **HTML Parsing** | `BeautifulSoup4` + `lxml` - Fast parsing |
| **Data Processing** | `pandas` - Clean CSV export |
| **Sheets API** | `gspread` + `google-auth` - OAuth2 |
| **Scheduling** | `APScheduler` - Cron-style jobs |

**Why These Choices?**
- ✅ Fast: Async scraping handles 50+ URLs concurrently
- ✅ Reliable: Robust error handling and retries
- ✅ Simple: Single Python file, no complex setup
- ✅ Extensible: Easy to add new sources

---

## 📂 Project Structure

```
data-sentry/
├── scraper.py           # Main scraper (single file!)
├── config.yaml          # Easy configuration
├── requirements.txt     # Dependencies
├── data/               # CSV output files
├── credentials/        # Google Sheets credentials
├── docs/HLD.md        # Future expansion plans
└── README.md          # You are here
```

---

## 🚀 Roadmap

### ✅ MVP (Current)
- [x] Async scraping (HN, PH, Reddit)
- [x] CSV export
- [x] Basic configuration

### 🔄 Phase 2 (Next Week)
- [ ] Google Sheets sync
- [ ] Email alerts
- [ ] Automated scheduling
- [ ] Change detection

### 🎯 Phase 3 (Future)
- [ ] Custom website scraping
- [ ] Proxy rotation
- [ ] Web dashboard
- [ ] Database storage

---

## 🤝 Contributing

Have ideas? Found a bug? 

1. Fork the repo
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing`)
5. Open Pull Request

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file

Free for commercial and personal use. Attribution appreciated! 

---

## 💰 Hire Me

Need a custom scraper built? I deliver production-grade data automation solutions:

**Typical Projects:**
- Simple scraper (1-3 sites): **$150-$300**
- Google Sheets integration: **+$100**
- Automated scheduling: **+$100**
- Email/Slack alerts: **+$50**
- Custom data processing: **$200-$500**

**Full platforms:** $1,000-$5,000 (multi-site, dashboards, APIs)

📧 Contact: alihaidar2950@gmail.com  
💼 Portfolio: https://github.com/alihaidar2950

---

## 🙏 Acknowledgments

Built with:
- [aiohttp](https://docs.aiohttp.org/) - Async HTTP magic
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML parsing legend
- [pandas](https://pandas.pydata.org/) - Data wrangling powerhouse

---

**⭐ Star this repo if you find it useful!**

Made with ☕ by [Ali Haidar](https://github.com/alihaidar2950)

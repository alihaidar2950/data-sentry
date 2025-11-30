# 🔥 Data Sentry

> **High-Performance Business Data Scraper with Real-Time Google Sheets Automation**

A production-grade data automation system that continuously monitors websites, extracts structured business data at scale, cleans it, stores it, syncs it to Google Sheets, and triggers intelligent alerts when critical changes occur.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Quality](https://img.shields.io/badge/Code%20Quality-Production-brightgreen.svg)]()

---

## 🎯 Why Data Sentry?

Unlike basic web scrapers, **Data Sentry** is engineered for real business needs:

- ✅ **E-commerce sellers** tracking competitor pricing
- ✅ **Real estate investors** monitoring new listings
- ✅ **Price arbitrage traders** detecting opportunities
- ✅ **Marketing teams** gathering market intelligence
- ✅ **Local businesses** automating supplier price updates

This isn't a toy scraper — it's a **backend automation service** built with senior-level engineering practices.

---

## ⚡ Core Features

### 🚀 **Async High-Speed Web Scraping**
- Concurrent scraping of hundreds of pages using `asyncio` and `aiohttp`
- Smart retry logic with exponential backoff
- Configurable rate limiting to prevent bans
- User-defined CSS/XPath selectors
- Customizable crawl depth

### 🧹 **Intelligent Data Cleaning & Normalization**
- Currency normalization across formats
- Missing field handling
- Duplicate detection and removal
- Robust HTML parsing and cleanup
- Type conversion and validation

### 💾 **Flexible Storage Options**
- CSV export for quick analysis
- SQLite database for historical tracking
- Data versioning and diff comparison
- Query interface for historical data

### 📊 **Google Sheets Integration**
- OAuth2 authenticated API access
- Auto-create and manage sheets
- Real-time data synchronization
- Bulk insert and update operations
- Optional conditional formatting

### 🔔 **Smart Change Detection & Alerts**
- Price change monitoring
- Stock status tracking
- New listing detection
- Removed product alerts
- Multi-channel notifications (Email, Slack, Discord)

---

## 🔥 Advanced Features

### 🌐 **Proxy Rotation System**
- Support for free and premium proxy services
- Automatic rotation to prevent IP bans
- User-agent randomization
- Session management

### 🔐 **Authenticated Scraping**
- Login to member-only sites
- Cookie persistence
- Session handling
- Headless browser fallback (Playwright/Selenium)

### ⏰ **Built-in Scheduler**
- Cron-style job scheduling
- Intervals: 5 min, hourly, daily, weekly
- Background task execution
- Parallel job management

### 🌐 **REST API Control Layer** *(Optional)*
- FastAPI-powered endpoints
- Start/stop scraping jobs
- Query data exports
- Configure alerts
- Real-time status monitoring

### 🐳 **Dockerized Deployment**
- Production-ready `Dockerfile`
- `docker-compose.yml` for one-command startup
- Environment variable configuration
- Volume mounting for data persistence

---

## 🏗️ Project Architecture

```
data-sentry/
├── scraper/              # Core scraping engine
│   ├── fetcher.py        # Async HTTP fetching
│   ├── parser.py         # HTML/JSON parsing
│   └── normalizer.py     # Data cleaning & validation
├── storage/              # Data persistence layer
│   ├── csv_store.py      # CSV export functionality
│   └── db_store.py       # SQLite database operations
├── sheets/               # Google Sheets integration
│   └── sync.py           # OAuth2 + API sync logic
├── alerts/               # Notification system
│   ├── email.py          # SMTP email alerts
│   ├── slack.py          # Slack webhook integration
│   └── discord.py        # Discord webhook integration
├── api/                  # REST API (optional)
│   └── app.py            # FastAPI application
├── scheduler/            # Job scheduling
│   └── jobs.py           # Cron-style task runner
├── docker/               # Containerization
│   ├── Dockerfile
│   └── docker-compose.yml
├── tests/                # Unit & integration tests
├── config/               # Configuration files
├── logs/                 # Application logs
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Google Cloud account (for Sheets API)
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/alihaidar2950/data-sentry.git
cd data-sentry
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Google Sheets API**
- Create a project in [Google Cloud Console](https://console.cloud.google.com/)
- Enable Google Sheets API
- Download OAuth2 credentials JSON
- Place in `config/credentials.json`

5. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

6. **Run your first scrape**
```bash
python main.py --url https://example.com --selector ".product"
```

---

## 📖 Usage Examples

### Basic Scraping
```python
from scraper.fetcher import AsyncFetcher
from scraper.parser import HTMLParser

# Initialize scraper
fetcher = AsyncFetcher(max_concurrent=50)
parser = HTMLParser()

# Scrape data
urls = ["https://example.com/page1", "https://example.com/page2"]
raw_data = await fetcher.fetch_all(urls)
clean_data = parser.parse(raw_data, selector=".product")
```

### Google Sheets Sync
```python
from sheets.sync import SheetsSync

# Initialize sync
sync = SheetsSync(credentials_path="config/credentials.json")

# Create and populate sheet
sheet_id = sync.create_sheet("Product Prices")
sync.append_rows(sheet_id, clean_data)
```

### Alert Configuration
```python
from alerts.email import EmailAlert
from alerts.slack import SlackAlert

# Configure alerts
email = EmailAlert(smtp_config)
slack = SlackAlert(webhook_url)

# Send notifications
if price_changed:
    email.send("Price Alert", f"Price dropped to ${new_price}")
    slack.send(f"🚨 Price alert: ${new_price}")
```

---

## 🐳 Docker Deployment

```bash
# Build image
docker-compose build

# Run service
docker-compose up -d

# View logs
docker-compose logs -f

# Stop service
docker-compose down
```

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=scraper --cov-report=html

# Run specific test file
pytest tests/test_fetcher.py
```

---

## 📊 Real-World Use Cases

### 📦 **E-commerce Price Monitoring**
**Scenario**: Shopify seller tracks 5 competitors  
**Frequency**: Every 2 hours  
**Output**: Google Sheet with price changes highlighted  
**Value**: $500–$2,000

### 🏠 **Real Estate Deal Finder**
**Scenario**: Investor monitors new listings  
**Frequency**: Every 10 minutes  
**Alerts**: Instant Slack notification  
**Value**: $1,000+

### 💼 **Supplier Price Tracker**
**Scenario**: Local business tracks supplier pricing  
**Frequency**: Daily  
**Output**: Auto-updated reporting dashboard  
**Value**: $300–$800/month (recurring)

---

## 💰 Commercial Applications

This project is perfect for:

| Service Offering                 | Typical Price Range |
|----------------------------------|---------------------|
| Single scraper → CSV export      | $150–$300           |
| Scraper + Sheets + alerts        | $400–$900           |
| Full deployed automation service | $1,000–$2,500       |
| Monthly monitoring contract      | $200–$800/month     |

---

## 🛠️ Tech Stack

- **Core**: Python 3.9+, asyncio, aiohttp
- **Parsing**: BeautifulSoup4, lxml
- **Data**: pandas, SQLite
- **API**: FastAPI, Pydantic
- **Scheduling**: APScheduler
- **Cloud**: Google Sheets API, OAuth2
- **Alerts**: SMTP, Slack/Discord webhooks
- **Containerization**: Docker, docker-compose
- **Testing**: pytest, pytest-cov
- **Code Quality**: Black, flake8, mypy

---

## 🎯 Skills Demonstrated

This project showcases:

✅ **Async Python Programming** (asyncio, aiohttp)  
✅ **Concurrent Processing** (multithreading, parallel execution)  
✅ **API Integration** (Google Sheets, REST APIs)  
✅ **Data Engineering** (ETL pipelines, normalization)  
✅ **Backend Development** (FastAPI, service architecture)  
✅ **DevOps** (Docker, CI/CD, automation)  
✅ **Software Quality** (testing, static analysis, logging)  
✅ **Production Systems** (error handling, monitoring, alerts)

---

## 🗺️ Roadmap

- [ ] **Phase 1**: Core scraping engine + CSV export
- [ ] **Phase 2**: Google Sheets integration
- [ ] **Phase 3**: Alert system (email, Slack, Discord)
- [ ] **Phase 4**: Proxy rotation + anti-ban measures
- [ ] **Phase 5**: REST API layer
- [ ] **Phase 6**: Scheduler + background jobs
- [ ] **Phase 7**: Docker deployment
- [ ] **Phase 8**: Web UI dashboard (React/Vue)
- [ ] **Phase 9**: Cloud deployment (AWS/GCP/Azure)
- [ ] **Phase 10**: SaaS multi-tenant version

---

## 📝 Configuration

Create a `.env` file in the root directory:

```env
# Scraper Settings
MAX_CONCURRENT_REQUESTS=50
REQUEST_TIMEOUT=30
RETRY_ATTEMPTS=3
RATE_LIMIT_DELAY=1

# Google Sheets
GOOGLE_CREDENTIALS_PATH=config/credentials.json
DEFAULT_SHEET_NAME=Scraped Data

# Database
DATABASE_PATH=data/scraper.db

# Alerts
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR/WEBHOOK

# Scheduler
SCRAPE_INTERVAL=3600  # seconds
ENABLE_SCHEDULER=true

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/scraper.log
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ali Haidar**
- GitHub: [@alihaidar2950](https://github.com/alihaidar2950)
- Email: alihaidar2950@gmail.com

---

## 🌟 Acknowledgments

Built with modern Python best practices and production-grade engineering standards. Perfect for:
- Backend Engineer roles
- Data Engineer positions
- Python Automation Engineer jobs
- Freelance scraping projects
- Startup automation contracts

---

## 📞 Support & Services

Looking for custom scraping solutions or automation services?

**Available for:**
- Custom web scraping projects
- Data automation consulting
- API integration services
- Backend system development

**Contact:** alihaidar2950@gmail.com

---

<div align="center">

**⭐ Star this repo if you find it useful!**

Made with ❤️ by Ali Haidar

</div>

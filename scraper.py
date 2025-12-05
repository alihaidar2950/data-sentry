"""
Data Sentry - Simple Business Data Scraper
Scrapes Hacker News, Product Hunt, and Reddit for trending content
"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
from pathlib import Path
from typing import List, Dict
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DataSentry:
    """Main scraper class"""
    
    def __init__(self):
        self.session = None
        self.data_dir = Path("data")
        self.data_dir.mkdir(exist_ok=True)
        
    async def __aenter__(self):
        """Setup async session"""
        self.session = aiohttp.ClientSession(
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Cleanup async session"""
        if self.session:
            await self.session.close()
    
    async def fetch_page(self, url: str) -> str:
        """Fetch a single page with error handling"""
        try:
            async with self.session.get(url, timeout=30) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    logger.error(f"Failed to fetch {url}: Status {response.status}")
                    return None
        except Exception as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return None
    
    async def scrape_hackernews(self) -> List[Dict]:
        """Scrape top stories from Hacker News"""
        logger.info("Scraping Hacker News...")
        url = "https://news.ycombinator.com/"
        html = await self.fetch_page(url)
        
        if not html:
            return []
        
        soup = BeautifulSoup(html, 'html.parser')
        stories = []
        
        # Find all story rows
        story_rows = soup.select('tr.athing')[:30]  # Top 30 stories
        
        for row in story_rows:
            try:
                title_cell = row.select_one('span.titleline > a')
                score_row = row.find_next_sibling('tr')
                
                if title_cell and score_row:
                    title = title_cell.text.strip()
                    link = title_cell.get('href', '')
                    
                    # Make relative URLs absolute
                    if link.startswith('item?'):
                        link = f"https://news.ycombinator.com/{link}"
                    
                    score_elem = score_row.select_one('span.score')
                    score = score_elem.text.replace(' points', '') if score_elem else '0'
                    
                    stories.append({
                        'source': 'Hacker News',
                        'title': title,
                        'url': link,
                        'score': score,
                        'scraped_at': datetime.now().isoformat()
                    })
            except Exception as e:
                logger.warning(f"Error parsing HN story: {str(e)}")
                continue
        
        logger.info(f"Found {len(stories)} Hacker News stories")
        return stories
    
    async def scrape_producthunt(self) -> List[Dict]:
        """Scrape trending products from Product Hunt"""
        logger.info("Scraping Product Hunt...")
        url = "https://www.producthunt.com/"
        html = await self.fetch_page(url)
        
        if not html:
            return []
        
        soup = BeautifulSoup(html, 'html.parser')
        products = []
        
        # Product Hunt uses dynamic loading, so we'll get what we can from initial HTML
        # In a production version, you might use Selenium or their API
        product_cards = soup.select('a[href*="/posts/"]')[:20]
        
        for card in product_cards:
            try:
                title = card.get_text(strip=True)
                link = card.get('href', '')
                
                if link and not link.startswith('http'):
                    link = f"https://www.producthunt.com{link}"
                
                if title and link and len(title) > 3:  # Filter out empty/short titles
                    products.append({
                        'source': 'Product Hunt',
                        'title': title,
                        'url': link,
                        'score': 'N/A',
                        'scraped_at': datetime.now().isoformat()
                    })
            except Exception as e:
                logger.warning(f"Error parsing PH product: {str(e)}")
                continue
        
        # Remove duplicates based on URL
        seen_urls = set()
        unique_products = []
        for p in products:
            if p['url'] not in seen_urls:
                seen_urls.add(p['url'])
                unique_products.append(p)
        
        logger.info(f"Found {len(unique_products)} Product Hunt products")
        return unique_products
    
    async def scrape_reddit(self, subreddit: str = "technology") -> List[Dict]:
        """Scrape top posts from a subreddit"""
        logger.info(f"Scraping Reddit r/{subreddit}...")
        url = f"https://old.reddit.com/r/{subreddit}/hot/"
        html = await self.fetch_page(url)
        
        if not html:
            return []
        
        soup = BeautifulSoup(html, 'html.parser')
        posts = []
        
        # Find all post containers
        post_divs = soup.select('div.thing[data-type="link"]')[:25]
        
        for div in post_divs:
            try:
                title_elem = div.select_one('a.title')
                score_elem = div.select_one('div.score.unvoted')
                
                if title_elem:
                    title = title_elem.text.strip()
                    link = title_elem.get('href', '')
                    score = score_elem.get('title', '0') if score_elem else '0'
                    
                    # Make relative URLs absolute
                    if link.startswith('/r/'):
                        link = f"https://old.reddit.com{link}"
                    
                    posts.append({
                        'source': f'Reddit r/{subreddit}',
                        'title': title,
                        'url': link,
                        'score': score,
                        'scraped_at': datetime.now().isoformat()
                    })
            except Exception as e:
                logger.warning(f"Error parsing Reddit post: {str(e)}")
                continue
        
        logger.info(f"Found {len(posts)} Reddit posts")
        return posts
    
    async def scrape_all(self) -> pd.DataFrame:
        """Scrape all sources concurrently"""
        logger.info("Starting scraping all sources...")
        
        # Run all scrapers concurrently
        results = await asyncio.gather(
            self.scrape_hackernews(),
            self.scrape_producthunt(),
            self.scrape_reddit("technology"),
            self.scrape_reddit("programming"),
        )
        
        # Flatten results
        all_data = []
        for result in results:
            all_data.extend(result)
        
        # Convert to DataFrame
        df = pd.DataFrame(all_data)
        logger.info(f"Total items scraped: {len(df)}")
        
        return df
    
    def save_to_csv(self, df: pd.DataFrame) -> str:
        """Save data to timestamped CSV file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.data_dir / f"scraped_data_{timestamp}.csv"
        
        df.to_csv(filename, index=False)
        logger.info(f"Saved data to {filename}")
        
        return str(filename)


async def main():
    """Main execution function"""
    async with DataSentry() as scraper:
        # Scrape all sources
        df = await scraper.scrape_all()
        
        # Save to CSV
        if not df.empty:
            csv_file = scraper.save_to_csv(df)
            print(f"\n✅ Scraping complete!")
            print(f"📊 Total items: {len(df)}")
            print(f"💾 Saved to: {csv_file}")
            
            # Show sample data
            print(f"\n📝 Sample data:")
            print(df.head(10).to_string())
        else:
            print("❌ No data scraped")


if __name__ == "__main__":
    asyncio.run(main())

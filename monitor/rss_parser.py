import aiohttp
import feedparser


async def fetch_rss(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def parse_rss(url):
    rss_data = await fetch_rss(url)
    feed = feedparser.parse(rss_data)
    return feed.entries  # Возвращает список статей

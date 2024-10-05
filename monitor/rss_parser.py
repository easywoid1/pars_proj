import aiohttp
import feedparser
import asyncio

async def main():
    url = 'https://news.ru/rss/category/article/russia/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            try:
                response.raise_for_status()  # Вызывает исключение, если статус не 200
                return await response.text()
            except aiohttp.ClientResponseError as e:
                print(f"HTTP Error: {e}")  # Обработка исключения
                return None  # Вернуть None или другое значение, чтобы указать на ошибку

# async def parse_rss(url):
#     rss_data = await fetch_rss(url)
#     if rss_data is None:
#         return []  # Вернуть пустой список, если ошибка
#     feed = feedparser.parse(rss_data)
#     return feed.entries  # Возвращает список статей
#
# async def main():
#     url = "https://news.ru/rss/type/post/"  # Укажите URL вашего RSS-канала
#     articles = await parse_rss(url)
#     if not articles:
#         print("No articles found or there was an error.")
#         return
#     for article in articles:
#         print(f"Title: {article.title}")
#         print(f"Link: {article.link}")
#         print(f"Published: {article.published}")
#         print("-----")

if __name__ == "__main__":
    asyncio.run(main())

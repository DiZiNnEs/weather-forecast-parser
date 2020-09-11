import aiohttp
import asyncio
from aiohttp.client import ClientTimeout

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
url = 'https://www.gismeteo.kz/weather-kirgizovo-197163/month/'


async def request(url: str, headers: str) -> None:
    session = aiohttp.ClientSession()
    async with session.get(url=url, headers=headers) as response:
        print(response.status)
        print(await response.text())

    await session.close()


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://www.gismeteo.kz/weather-kirgizovo-197163/month/')
        print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(request(url, user_agent))

from bs4 import BeautifulSoup

from typing import Dict, Any, Coroutine

import aiohttp
import asyncio

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
url = 'https://www.gismeteo.kz/weather-kokshetau-4616/month/'


async def request(url_: str, headers: Dict) -> str:
    session = aiohttp.ClientSession()

    async with session.get(url=url_, headers=headers) as response:
        content = await response.text()
        # content_len = len(await response.text())  # 337550

    await session.close()

    return content


def html_processing() -> None:
    print('Hello')
    soup = BeautifulSoup(request(url, user_agent), 'html.parser')
    for html in soup.find_all('div'):
        print(html)


async def start() -> None:
    print('Hello')
    html_processing()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(len(loop.run_until_complete(request(url, user_agent))))
    # loop.run_until_complete(request(url, user_agent))
    # html_processing(start())
    loop.create_task(html_processing())
    # asyncio.create_task(start())

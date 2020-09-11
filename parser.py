from typing import Set

import aiohttp
import asyncio

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
url = 'https://www.gismeteo.kz/weather-kirgizovo-197163/month/'


async def request(url_: str, headers: Set[str]) -> None:
    session = aiohttp.ClientSession()

    async with session.get(url=url_, headers=headers) as response:
        print(response.status)
        print(await response.text())

    await session.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(request(url, user_agent))

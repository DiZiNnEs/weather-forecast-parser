from aiohttp import ClientSession
from asyncio import get_event_loop

from dotenv import load_dotenv

from typing import (
    Dict,
)

import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

url = f'https://api.openweathermap.org/data/2.5/onecall?lat=53.2871&lon=69.4044&exclude=weekly&appid={API_KEY}'


async def request(url_: str, headers: Dict) -> str:
    """
    This function make async request to web-site
    :param url_: str
    :param headers: Dict[str: str]
    :return: HTML[str]
    """
    session = ClientSession()
    async with session.get(url=url_, headers=headers) as response:
        content = await response.text()
    await session.close()

    return content


async def response(response_text: str) -> None:
    pass


if __name__ == '__main__':
    loop = get_event_loop()
    print(loop.run_until_complete(request(url_=url, headers=user_agent)))

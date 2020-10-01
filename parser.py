import json

from aiohttp import ClientSession
from asyncio import get_event_loop

from dotenv import load_dotenv

from typing import (
    Dict,
    Coroutine,
    Any,
)

import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

url = f'https://api.openweathermap.org/data/2.5/onecall?lat=53.2871&lon=69.4044&exclude=weekly&appid={API_KEY}'


async def request() -> str:
    """
    This function make async request to web-site
    :return: HTML[str]
    """
    session = ClientSession()
    async with session.get(url=url, headers=user_agent) as response_from_server:
        content = await response_from_server.text()
    await session.close()

    return content


async def response(response_text: str) -> str:
    """
    This function handle response
    :param response_text: str
    :return: None
    """
    load_json = json.loads(response_text)
    unload_json = json.dumps(load_json, indent=4)
    return unload_json


async def cli():
    print('Hello')
    print('Result of parse:')
    print(await response(await request()))
    test = await response(await request())


if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(cli())

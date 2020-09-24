from aiohttp import ClientSession
from asyncio import get_event_loop

from bs4 import BeautifulSoup

from typing import (
    Dict,
    List,
    Coroutine,
    Any
)

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
url = 'https://www.meteoguru.com/en/pro/forecast/?latlon=51.1605,71.4704'


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


async def html_processing() -> List[str]:
    """
    This function processing html from function request
    :return: List[str]
    """
    soup = BeautifulSoup(await request(url, user_agent), 'html.parser')
    result = []
    weathers = ['Пасмурно, дождь', 'Облачно, небольшой дождь', 'Пасмурно, небольшой дождь', 'Пасмурно, сильный дождь',
                'Переменная облачность, небольшой дождь', 'Пасмурно, сильный дождь, гроза',
                'Малооблачно, небольшой дождь',
                'Пасмурно, дождь, гроза', 'Облачно, небольшой дождь, гроза', 'Малооблачно, небольшой дождь']
    for looking_rain in soup.find_all(attrs={'data-text': weathers}):
        if looking_rain['data-text'] is not None:
            result.append(looking_rain['data-text'])
        else:
            result.append('It won\'t rain this month')
    return result


async def output_weathers(result: Coroutine[Any, Any, List[str]]) -> List[str]:
    """
    This function serves for output result weathers
    :param result: Coroutine[Any, Any, List[str]
    :return: None
    """
    weathers_ = await result
    weathers = list(set(weathers_))
    weather_list = []
    for for_weather in weathers:
        weather_list.append(f'Погода: "{for_weather}" будет около {weathers_.count(for_weather)} раза')

    for x in weather_list:
        print(x)
    return weather_list


if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(output_weathers(html_processing()))

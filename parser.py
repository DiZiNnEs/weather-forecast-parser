from aiohttp import ClientSession
from asyncio import get_event_loop

from bs4 import BeautifulSoup

from typing import Dict, List, Coroutine, Any

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
url = 'https://www.gismeteo.kz/weather-kokshetau-4616/month/'


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
    weathers = ['Пасмурно, дождь', 'Облачно, небольшой дождь', 'Пасмурно, небольшой дождь',
                'Переменная облачность, небольшой дождь',
                'Пасмурно, дождь, гроза', 'Облачно, небольшой дождь, гроза', 'Малооблачно, небольшой дождь']
    for looking_rain in soup.find_all(attrs={'data-text': weathers}):
        if looking_rain['data-text'] is not None:
            result.append(looking_rain['data-text'])
        else:
            result.append('It won\'t rain this month')
    return result


async def output_weathers(result: Coroutine[Any, Any, List[str]]) -> None:
    """
    This function serves for output result weathers
    :param result: Coroutine[Any, Any, List[str]
    :return: None
    """
    weather = await result
    a = 1
    for x in weather:
        print(x, x.count(x), a)
        a += 1

    print(len(weather))
    print('Пасмурно и дождь ожидается: ', weather.count('Пасмурно, дождь'))
    print('Облачно и небольшой дождь ожидается: ', weather.count('Облачно, небольшой дождь'))
    print('Пасмурно и небольшой дождь ожидается: ', weather.count('Пасмурно, небольшой дождь'))
    print('Переменная облачность и небольшой дождь ожидается: ',
          weather.count('Переменная облачность, небольшой дождь'))
    print('Ожидается дождь и гроза около: ', weather.count('Пасмурно, дождь, гроза'))
    print('Облачно и небольшой дождь с грозой ожидается: ', weather.count('Облачно, небольшой дождь, гроза'))
    print('Малооблачно с небольшим дождём ожидается около: ', weather.count('Малооблачно, небольшой дождь'))


if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(output_weathers(html_processing()))

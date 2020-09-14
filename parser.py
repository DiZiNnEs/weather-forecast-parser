from aiohttp import ClientSession
from asyncio import get_event_loop

from bs4 import BeautifulSoup

from typing import Dict, List

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
url = 'https://www.gismeteo.kz/weather-kokshetau-4616/month/'


async def request(url_: str, headers: Dict) -> str:
    session = ClientSession()
    async with session.get(url=url_, headers=headers) as response:
        content = await response.text()
    await session.close()

    return content


async def html_processing() -> List[str]:
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


async def conclusion():
    pass


if __name__ == '__main__':
    loop = get_event_loop()
    print(len(loop.run_until_complete(html_processing())))

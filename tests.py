import unittest
import parser

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
url = 'https://www.gismeteo.kz/weather-kirgizovo-197163/month/'


class MyTestCase(unittest.TestCase):
    async def request_test(self):
        result = await parser.request(url, user_agent)
        self.assertEqual(result, 335873)


if __name__ == '__main__':
    unittest.main()

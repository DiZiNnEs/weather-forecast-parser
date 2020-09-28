import parser
from unittest import main
from aiounittest import AsyncTestCase


class MyTestCase(AsyncTestCase):

    async def test_request(self):
        print(1)
        result = await parser.request()
        self.assertEqual(True, len(result) > 13000)

    async def test_parser(self):
        print(2)
        request = await parser.request()
        result = await parser.response(response_text=request)
        self.assertEqual(True, len(result) > 30000)


if __name__ == '__main__':
    main()

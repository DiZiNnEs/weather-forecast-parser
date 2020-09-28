import parser
from unittest import main
from aiounittest import AsyncTestCase


class MyTestCase(AsyncTestCase):

    async def test_parser(self):
        request = await parser.request()
        result = await parser.response(response_text=request)
        self.assertEqual(True, len(result) > 30000)


if __name__ == '__main__':
    main()

import parser


from unittest import main
from aiounittest import AsyncTestCase


class MyTestCase(AsyncTestCase):
    async def test_parser(self):
        result = await parser.request(parser.url, parser.user_agent)
        self.assertEqual(len(result), 332418)


if __name__ == '__main__':
    main()
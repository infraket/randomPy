import unittest
import string
from main import generate_short_url


class TestUrlGenerator(unittest.TestCase):

    def test_length(self):
        """Проверяем, что функция возвращает строку нужной длины"""
        length = 10
        result = generate_short_url(length=length)

        self.assertEqual(len(result), length)

    def test_allowed_characters(self):
        """Проверяем, что в ссылке только буквы и цифры"""
        allowed_chars = set(string.ascii_letters + string.digits)
        result = generate_short_url()

        for char in result:
            self.assertIn(char, allowed_chars)


if __name__ == '__main__':
    unittest.main()

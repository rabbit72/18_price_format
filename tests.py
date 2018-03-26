import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_float_str(self):
        self.assertEqual(format_price('3245.000000'), '3 245')

    def test_int_str(self):
        self.assertEqual(format_price('3245'), '3 245')

    def test_float_value(self):
        self.assertEqual(format_price(3245.000000), '3 245')

    def test_int_value(self):
        self.assertEqual(format_price(3245), '3 245')

    def test_string_text(self):
        self.assertEqual(format_price('test'), None)


if __name__ == '__main__':
    unittest.main()
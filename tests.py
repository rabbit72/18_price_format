import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_float_str(self):
        self.assertEqual(format_price('3245.000000'), '3 245')

    def test_float_value(self):
        self.assertEqual(format_price(3245.50000), '3 245')

    def test_negative_float(self):
        self.assertEqual(format_price(-3245.400000), '-3 245')

    def test_int_str(self):
        self.assertEqual(format_price('3245'), '3 245')

    def test_int_value(self):
        self.assertEqual(format_price(3245), '3 245')

    def test_negative_int(self):
        self.assertEqual(format_price(-3245), '-3 245')

    def test_string_text(self):
        self.assertEqual(format_price('t55est'), None)

    def test_string_int_long_number(self):
        self.assertEqual(format_price('100_000_000'), '100 000 000')

    def test_int_long_number(self):
        self.assertEqual(format_price(100_000_000), '100 000 000')

    def test_string_float_long_number(self):
        self.assertEqual(format_price('100_000_000.4444'), '100 000 000')

    def test_float_long_number(self):
        self.assertEqual(format_price(100_000_000.60), '100 000 000')


if __name__ == '__main__':
    unittest.main()
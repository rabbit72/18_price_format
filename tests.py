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

    def test_long_number(self):
        self.assertEqual(format_price('56_564_54_44__55555'), None)

    def test_bool(self):
        self.assertEqual(format_price(True), None)

    def test_none(self):
        self.assertEqual(format_price(None), None)

    def test_list(self):
        self.assertEqual(format_price([1, 2]), None)

    def test_empty_str(self):
        self.assertEqual(format_price(''), None)


if __name__ == '__main__':
    unittest.main()
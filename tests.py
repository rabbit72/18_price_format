import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_float_str_1(self):
        self.assertEqual(format_price('3245.000000'), '3 245')

    def test_float_str_2(self):
        self.assertEqual(format_price('3245.0000001'), '3 245')

    def test_float_str_3(self):
        self.assertEqual(format_price('3245.0000000000001'), '3 245')

    def test_float_str_4(self):
        self.assertEqual(format_price('0.0000000000001'), '0')

    def test_float_less_1_str(self):
        self.assertEqual(format_price('0.34234324'), '0.34')

    def test_float_value_1(self):
        self.assertEqual(format_price(3245.556666666), '3 245.56')

    def test_float_value_2(self):
        self.assertEqual(format_price(3245.00000000000005), '3 245')

    def test_float_value_3(self):
        self.assertEqual(format_price(0.0049), '0')

    def test_float_value_4(self):
        self.assertEqual(format_price(0.005), '0.01')

    def test_float_value_5(self):
        self.assertEqual(format_price(0.0000000000000), '0')

    def test_negative_float(self):
        self.assertEqual(format_price(-3245.444), '-3 245.44')

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
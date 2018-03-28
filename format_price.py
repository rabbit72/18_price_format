import sys


def is_integer(number):
    minimum_value_for_int = 0.005
    fractional_remainder = number % 1
    if fractional_remainder < minimum_value_for_int:
        return True


def format_price(price):
    if isinstance(price, bool):
        return None
    try:
        price_as_number = float(price)
    except (ValueError, TypeError):
        return None
    if is_integer(price_as_number):
        str_price = '{0:,}'.format(int(price_as_number))
    else:
        str_price = '{0:,.2f}'.format(price_as_number)
    return str_price.replace(',', ' ')


if __name__ == '__main__':
    try:
        str_price = format_price(sys.argv[1])
        if not str_price:
            print("Can't be converted")
        else:
            print(str_price)
    except IndexError:
        print('Not entered price')

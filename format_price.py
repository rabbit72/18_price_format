import sys


def format_price(price):
    if isinstance(price, bool):
        return None
    try:
        price_as_number = float(price)
        return '{0:,g}'.format(price_as_number).replace(',', ' ')
    except (ValueError, TypeError):
        return None


if __name__ == '__main__':
    try:
        str_price = format_price(sys.argv[1])
        if not str_price:
            print("Can't be converted")
        else:
            print(str_price)
    except IndexError:
        print('Not entered price')

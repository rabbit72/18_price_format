import sys


def format_price(price):
    if isinstance(price, bool):
        return None
    try:
        price_as_number = int(float(price))
    except (ValueError, TypeError):
        return None
    return '{0:,}'.format(price_as_number).replace(',', ' ')


if __name__ == '__main__':
    try:
        str_price = format_price(sys.argv[1])
        if not str_price:
            print("Can't be converted")
        else:
            print(str_price)
    except IndexError:
        print('Not entered price')

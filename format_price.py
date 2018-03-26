import sys


def format_price(price):
    try:
        price_is_number = int(float(price))
    except ValueError:
        return None
    return '{0:,}'.format(price_is_number).replace(',', ' ')


if __name__ == '__main__':
    try:
        str_price = format_price(sys.argv[1])
        if not str_price:
            print("Can't be converted")
        else:
            print(str_price)
    except IndexError:
        print('Not entered price')

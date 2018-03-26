import sys
import locale
from unicodedata import normalize


def format_price(price):
    try:
        number_price = float(price)
    except ValueError:
        return None
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    str_price = locale.format_string('%d', number_price, grouping=True)
    return normalize("NFKD", str_price)


if __name__ == '__main__':
    try:
        answer = format_price(sys.argv[1])
        if not answer:
            print("Can't be converted")
        else:
            print(answer)
    except IndexError:
        print('Not entered price')

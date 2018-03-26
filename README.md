# Price Formatter

This module need for price formatting.

# How install 
Python 3 should be already installed.

# Quick start

```bash
$ python3 format_price.py <price>
```
Running on Windows is similar.

*(Possibly requires call of 'python' executive instead of just 'python3'.)*

# How use
```python
>>> from format_price import format_price 
>>> format_price(3333333333)
'3 333 333 333'

>>> format_price('444444444')
'444 444 444'

>>> format_price('4444.0000000')
'4 444'

>>> print(format_price('Error'))
None
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

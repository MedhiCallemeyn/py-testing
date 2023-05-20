# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
# In app folder do: python -m pytest tests 
from app import utils
import pytest

def test_discount_price_25_10():
    # Arrange 
    price = '25.00€'
    discount = 10
    #Act   ---->   Assert
    assert utils.discount_price(price,discount) == '22.5€'

def test_discount_price_55_130():
    # Arrange 
    price = '55.00€'
    discount = 130

    #Act   ---->   Assert
    with pytest.raises(ValueError):
        utils.discount_price(price,discount)


def test_discount_price_32e52_55():
    # Arrange 
    price = '32.52€'
    discount = 55
    #Act   ---->   Assert
    assert utils.discount_price(price,discount) == '17.88€'

def test_discount_prices_13e66_52e16_30():
    prices = ['13.66€','52.16€']
    discount = 30

    assert utils.discount_prices(prices,discount) == ['4.09€','15.64€']
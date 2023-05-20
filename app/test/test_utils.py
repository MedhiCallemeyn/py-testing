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



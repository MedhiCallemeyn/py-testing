




def discount_price(price:str,discount:float,currency:str = '€')-> str:
    
    if not 0 < discount <100:
      raise ValueError('Invalid discount values')

    multiplier = (100-discount)/100
    price_discounted = float(price.replace(currency,''))*multiplier
    price_rounded = round(price_discounted, 2)
    return f'{price_rounded}{currency}'


def discount_prices(prices:list[str],discount:float,currency:str = '€')->list[str]:
    return [discount_price(price,discount,currency) for price in list]


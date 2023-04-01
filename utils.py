import requests
import json
from extensions import keys

class ConvertionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Нет смысла переводить из {quote} в {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Неправильно введено название валюты "{quote}"')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Неправильно введено название валюты "{base}"')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Неправильно введено количество валюты')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
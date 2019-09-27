import requests
import json

from api.controllers import requestQuoteCoins as conversion
from api.controllers.helpers import convertDate as conversion_date
# import requestQuoteCoins as conversion
# import helpers.convertDate as conversion_date

PATH_EXCHANGE_RATE = 'https://rest.coinapi.io/v1/exchangerate'
API_AUTH = 'D8521ADC-FBB3-4426-8F53-C24158590197'

quote_brl = conversion.USD_to_BRL()


def simulation(**kwargs):
    baseInvestiment = kwargs.get('baseInvestiment', 50)
    initialDate = kwargs.get('initialDate', False)
    finalDate = kwargs.get('finalDate', False)
    _assetBase = kwargs.get('asset', 'BTC')
    assetBase = 'BTC' if _assetBase == 'BTC' else _assetBase.split('/')[0]
    _assetQuote = kwargs.get('asset', 'USD')
    assetQuote = 'USD' if _assetQuote == 'USD' else _assetBase.split('/')[1]

    params = {
        'apikey': API_AUTH
    }

    if initialDate:
        params['time'] = initialDate
        response = requests.get(
            f'{PATH_EXCHANGE_RATE}/{assetBase}/{assetQuote}',
            params=params)
        response.encoding = 'utf-8'
        data_initial = response.json()

    if finalDate:
        params['time'] = finalDate
        response = requests.get(
            f'{PATH_EXCHANGE_RATE}/{assetBase}/{assetQuote}',
            params=params)
        response.encoding = 'utf-8'
        data_final = response.json()

    else:
        return {
            'message': 'PARAMETERS_ERROR'
        }

    # Cálculo da simulação
    buyPrice = float(data_initial['rate'])*quote_brl
    sellPrice = float(data_final['rate'])*quote_brl

    gainPercentage = (sellPrice/buyPrice)
    gainPrice = (baseInvestiment*gainPercentage)
    quantityCryptoPast = (baseInvestiment/buyPrice)
    quantityCryptoToday = (baseInvestiment/sellPrice)
    gainPercentage = round((gainPercentage-1), 2)*100

    return {
        'market': f'{assetBase}/{assetQuote}',
        'asset_conversion': 'BRL',
        'buy_date': conversion_date.convert_ISO8601_to_normal(initialDate),
        'sell_date': conversion_date.convert_ISO8601_to_normal(finalDate),
        'buy_price': buyPrice,
        'sell_price': sellPrice,
        'base_investiment_fiat': baseInvestiment,
        'base_investiment_cripto': round(quantityCryptoPast, 8),
        'quantity_cripto_if_buy_today': round(quantityCryptoToday, 8),
        'profit_percentage': gainPercentage,
        'profit_fiat_price': round(gainPrice-baseInvestiment, 2),
        'fiat_total': round(gainPrice, 2)
    }


if __name__ == "__main__":
    print(simulation(initialDate='2017-09-24T12:00:00-03:00',
                     finalDate='2018-01-01T12:00:00-03:00'))

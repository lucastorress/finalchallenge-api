import requests
import json

PATH_EXCHANGE_RATE = 'https://rest.coinapi.io/v1/exchangerate'
API_AUTH = 'D8521ADC-FBB3-4426-8F53-C24158590197'


def RegressiveSimulation(**kwargs):
    baseInvestiment = kwargs.get('baseInvestiment', 50)
    initialDate = kwargs.get('initialDate', False)
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

    # Caso não selecione data
    else:
        response = requests.get(
            f'{PATH_EXCHANGE_RATE}/{assetBase}/{assetQuote}',
            params=params)

    response.encoding = 'utf-8'
    data = response.json()

    params = {
        'apikey': API_AUTH
    }

    currentPrice = requests.get(
            f'{PATH_EXCHANGE_RATE}/{assetBase}/{assetQuote}',
            params=params)
    currentPrice.encoding = 'utf-8'
    currentPrice = currentPrice.json()

    # Cálculo da simulação
    pastPrice = float(data['rate'])
    currentPrice = float(currentPrice['rate'])

    gainPercentage = (currentPrice/pastPrice)
    gainPrice = (baseInvestiment*gainPercentage)
    quantityCryptoPast = (baseInvestiment/pastPrice)
    quantityCryptoToday = (baseInvestiment/currentPrice)
    gainPercentage = round((gainPercentage-1), 2)*100

    return {
        'market': f'{assetBase}/{assetQuote}',
        'initialDate': initialDate,
        'pastPrice': pastPrice,
        'currentPrice': currentPrice,
        'baseInvestiment': baseInvestiment,
        f'quantity{assetBase}_past': round(quantityCryptoPast, 8),
        f'quantity{assetBase}_today': round(quantityCryptoToday, 8),
        'gainPercentage': gainPercentage,
        f'gainPrice{assetQuote}': round(gainPrice-baseInvestiment, 2),
        'total': round(gainPrice, 2)
    }


if __name__ == "__main__":
    print(RegressiveSimulation())

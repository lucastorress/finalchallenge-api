import urllib3
import json

PATH_EXCHANGE_RATE = 'https://rest.coinapi.io/v1/exchangerate'
API_AUTH = 'D8521ADC-FBB3-4426-8F53-C24158590197'

urllib3.disable_warnings()
http = urllib3.PoolManager()


def RegressiveSimulation(**kwargs):
    baseInvestiment = kwargs.get('baseInvestiment', 50)
    initialDate = kwargs.get('initialDate', '2017-01-16T19:13:56-0300')
    _assetBase = kwargs.get('asset', 'BTC')
    assetBase = 'BTC' if _assetBase == 'BTC' else _assetBase.split('/')[0]
    _assetQuote = kwargs.get('asset', 'USD')
    assetQuote = 'USD' if _assetQuote == 'USD' else _assetBase.split('/')[1]

    if initialDate:
        response = http.request(
            'GET',
            f'{PATH_EXCHANGE_RATE}/{assetBase}/{assetQuote}?time={initialDate}',
            headers={
                'X-CoinAPI-Key': API_AUTH
            })
    # Caso não selecione data
    else:
        response = http.request(
            'GET',
            f'{PATH_EXCHANGE_RATE}/{assetBase}/{assetQuote}',
            headers={
                'X-CoinAPI-Key': API_AUTH
            })
    data = json.loads(response.data.decode('utf-8'))

    currentPrice = http.request(
        'GET',
        f'{PATH_EXCHANGE_RATE}/{assetBase}/{assetQuote}',
        headers={
            'X-CoinAPI-Key': API_AUTH
        })
    currentPrice = json.loads(currentPrice.data.decode('utf-8'))

    # Cálculo da simulação
    pastPrice = float(data['rate'])
    currentPrice = float(currentPrice['rate'])

    gainPercentage = (currentPrice/pastPrice)
    gainPrice = (baseInvestiment*gainPercentage)
    gainPercentage = round((gainPercentage-1), 2)*100

    return {
        'market': f'{assetBase}/{assetQuote}',
        'initialDate': initialDate,
        'pastPrice': pastPrice,
        'currentPrice': currentPrice,
        'baseInvestiment': baseInvestiment,
        'gainPercentage': gainPercentage,
        'gainPrice': round(gainPrice-baseInvestiment, 2),
        'total': round(gainPrice, 2)
    }

import requests
import json

# Config for CoinAPI
PATH_EXCHANGE_ASSETS = 'https://rest.coinapi.io/v1/assets'
API_AUTH_COINAPI = 'D8521ADC-FBB3-4426-8F53-C24158590197'
parameters_coinapi = {
    'apikey': API_AUTH_COINAPI
}

# Config for CoinMarketCap
PATH_LIST_COINS = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
API_AUTH_COINMARKETCAP = '39daf937-3857-4584-b8e8-437b48910269'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_AUTH_COINMARKETCAP,
}
parameters_coinmarketcap = {
        'limit': '10',
        'convert': 'BRL'
    }


def list_of_coins_simulation():
    try:
        response = requests.get(PATH_EXCHANGE_ASSETS,
                                params=parameters_coinapi)
        response.encoding = 'utf-8'
        data_coinapi = response.json()
    except:
        print("Exception... (CoinAPI)")
        return data_coinapi

    try:
        response = requests.get(PATH_LIST_COINS,
                                params=parameters_coinmarketcap,
                                headers=headers)
        response.encoding = 'utf-8'
        data_coinmarketcap = response.json()
        data_coinmarketcap = data_coinmarketcap['data']
    except:
        print("Exception... (CoinMarketCap)")
        return data_coinmarketcap

    assets = []

    for asset in data_coinapi:
        if asset['type_is_crypto'] == 1 and len(assets) <= 10:
            for asset_compare in data_coinmarketcap:
                if asset['asset_id'] == asset_compare['symbol']:
                    assets.append(asset['asset_id'])
                    break
        elif len(assets) == 10:
            print("Saindo da busca...")
            break

    return assets

if __name__ == "__main__":
    print(f'len({len(list_of_coins_simulation())}): {list_of_coins_simulation()}')

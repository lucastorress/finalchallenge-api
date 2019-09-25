import requests
import json

PATH_LIST_COINS = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
PATH_INFO_COINS = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
API_AUTH = '39daf937-3857-4584-b8e8-437b48910269'


headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_AUTH,
}


def list_of_coins():
    parameters = {
        'limit': '50',
        'convert': 'BRL'
    }

    response = requests.get(PATH_LIST_COINS,
                            params=parameters,
                            headers=headers)
    response.encoding = 'utf-8'
    data = response.json()
    _list = data['data']

    coins = []
    parameter_id = ''

    for i, coin in enumerate(_list):
        _id = coin['id']
        if i == len(_list)-1:
            parameter_id += f'{_id}'
        else:
            parameter_id += f'{_id},'

    parameters = {
        'id': parameter_id,
        'aux': 'logo,description'
    }

    try:
        response = requests.get(PATH_INFO_COINS,
                                params=parameters,
                                headers=headers)
        response.encoding = 'utf-8'
        data = response.json()
        print(f"Carregando... {i}")
        d = data['data']
    except:
        print('Except...')
        return data

    for i, coin in enumerate(_list):
        _id = coin['id']

        item = {
            'id': _id,
            'name': coin['name'],
            'symbol': coin['symbol'],
            'slug': coin['slug'],
            'logo': d[f'{_id}']['logo'],
            'description': d[f'{_id}']['description'],
            'rank': coin['cmc_rank'],
            'max_supply': coin['max_supply'],
            'circulating_supply': coin['circulating_supply'],
            'total_supply': coin['total_supply'],
            'price': coin['quote']['BRL']['price'],
            'volume_24h': coin['quote']['BRL']['volume_24h'],
            'percent_change_1h': coin['quote']['BRL']['percent_change_1h'],
            'percent_change_24h': coin['quote']['BRL']['percent_change_24h'],
            'percent_change_7d': coin['quote']['BRL']['percent_change_7d'],
            'market_cap': coin['quote']['BRL']['market_cap'],
        }
        coins.append(item)

    return coins

if __name__ == "__main__":
    print(list_of_coins())

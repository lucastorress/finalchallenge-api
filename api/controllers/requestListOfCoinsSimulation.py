import requests
import json

PATH_EXCHANGE_SYMBOLS = 'https://rest.coinapi.io/v1/assets'
API_AUTH = 'D8521ADC-FBB3-4426-8F53-C24158590197'

params = {
    'apikey': API_AUTH
}

response = requests.get(PATH_EXCHANGE_SYMBOLS,
                        params=params)
response.encoding = 'utf-8'
data = response.json()

print(data)

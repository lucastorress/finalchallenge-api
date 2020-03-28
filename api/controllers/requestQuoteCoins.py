import requests
import json

PATH_URL = 'https://economia.awesomeapi.com.br/all/USD-BRL'


def USD_to_BRL(debug=False):
    response = requests.get(PATH_URL)
    response.encoding = 'utf-8'
    data = response.json()

    if debug:
        return data

    brl = float(data['USD']['ask'])
    return float(round(brl, 2))

if __name__ == "__main__":
    print(USD_to_BRL())

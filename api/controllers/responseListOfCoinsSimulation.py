symbols = [
    'BTC',
    'ETH',
    'ETC',
    'LTC',
    'BCH',
    'XRP',
    'EOS',
    'BNB',
    'XLM',
    'XMR',
    'ADA',
    'TRX',
    'DASH',
    'ZEC',
    'DOGE',
    'NEO',
    'NANO',
    'IOTA'
]
names = [
    'Bitcoin',
    'Ethereum',
    'Ethereum Classic',
    'Litecoin',
    'Bitcoin Cash',
    'Ripple',
    'EOS',
    'Binance Coin',
    'Stellar',
    'Monero',
    'Cardano',
    'TRON',
    'Dash',
    'ZCash',
    'Dogecoin',
    'NEO',
    'Nano',
    'IOTA'
]


def response_list():
    response = []
    for i, item in enumerate(symbols):
        dic = {
            'id': i+1,
            'name': names[i],
            'symbol': item
        }

        response.append(dic)

    # for r in response:
    #     print(r)

    return response

if __name__ == "__main__":
    print(response_list())

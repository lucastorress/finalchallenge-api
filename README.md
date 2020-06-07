Apple Foundation - FinalChallenge API
=========================

Python API developed using Flask framework during process of Apple Foundation's class. Our team was composed by Raji, Albert and Lucas Torres. This API is used by mobile application developed in Swift and it's like a middleware.

## Installation
```sh
pip install -r requirements.txt
```

## Usage
With the requirements installed, you can write the following instruction to start API:
```sh
python3 run.py
```
Python 3 is recommended.

## Sample response from the server
Acess the API by the http://localhost:5000/ and get this response:
```json
{
    "message": "API is ready for use!",
    "url": [
        "/api/v1/simulation/<string:asset_id_base>/<int:value_base>/<string:buy_date>/<string:sell_date>",
        "/api/v1/simulation/",
        "/api/v1/simulationlist/",
        "/api/v1/ranklist",
        "/api/v1/latestnews"
    ]
}
```

## Simulation endpoint with errors
URL (GET only): http://localhost:5000/api/v1/simulation/
```json
{
    "message": "Fill in the fields correctly!",
    "url": "/api/v1/simulation/<string:asset_id_base>/<int:value_base>/<string:buy_date>/<string:sell_date>"
}
```

## Simulation endpoint
URL (GET only): http://localhost:5000/api/v1/simulation/BTC/5000/2017-09-01T12:00:00-0300/2018-09-01T12:00:00-0300

The default for buy_date and sell_date is ISO 8601.
```json
{
    "asset_conversion": "BRL",
    "base_investiment_cripto": 0.3278419,
    "base_investiment_fiat": 5000,
    "buy_date": "24/09/2017",
    "buy_price": 15251.253758351237,
    "fiat_total": 8942.6,
    "market": "BTC/USD",
    "profit_fiat_price": 3942.6,
    "profit_percentage": 79,
    "quantity_cripto_if_buy_today": 0.18330342,
    "sell_date": "24/09/2018",
    "sell_price": 27277.178136477036
}
```

## List of coins available for simulation
URL (GET only): http://localhost:5000/api/v1/simulationlist/
```json
{
    "simulationlist": [
        {
            "id": 1,
            "name": "Bitcoin",
            "symbol": "BTC"
        },
        ...
    ]
}
```

## List of top coins
URL (GET only): http://localhost:5000/api/v1/ranklist
```json
{
    "ranklist": [
        {
            "circulating_supply": 17955700,
            "description": "Bitcoin (BTC) is a consensus network that enables a new payment system and a completely digital currency. Powered by its users, it is a peer to peer payment network that requires no central authority to operate. On October 31st, 2008, an individual or group of individuals operating under the pseudonym \"Satoshi Nakamoto\" published the Bitcoin Whitepaper and described it as: \"a purely peer-to-peer version of electronic cash, which would allow online payments to be sent directly from one party to another without going through a financial institution.\"",
            "id": 1,
            "logo": "https://s2.coinmarketcap.com/static/img/coins/64x64/1.png",
            "market_cap": 638994363579.9025,
            "max_supply": 21000000,
            "name": "Bitcoin",
            "percent_change_1h": -1.06203079,
            "percent_change_24h": -12.45245236,
            "percent_change_7d": -14.83869769,
            "price": 35587.27109385334,
            "rank": 1,
            "slug": "bitcoin",
            "symbol": "BTC",
            "total_supply": 17955700,
            "volume_24h": 111453186207.8012
        },
        ...
    ]
}
```

## List of latest news in portuguese language
URL (GET only): http://localhost:5000/api/v1/latestnews

You can change the language on configuration.
```json
{
    "latestnews": [
        {
            "date": "2019-09-26T13:13:07.000Z",
            "description": "Os deputados federal aprovaram na quarta-feira (25) — em meio aos questionamentos ao CEO da Atlas Quantum — a audiência pública solicitada pela deputada federal Margarida Salomão (PT/MG). O objetivo é debater a regulamentação das criptomoedas e da tecnologia Blockchain. No dia anterior, a política…",
            "id": 1,
            "image_article": "https://portaldobitcoin.com/wp-content/uploads/2019/09/margarida-salomao2.png",
            "source": {
            "favicon": "https://assets.cryptocontrol.io/favicons/5bd00c580c38a7001921bdb2.png"
            },
            "title": "Comissão da Câmara para regular criptomoedas aprova audiência de deputada petista",
            "url": "https://cryptocontrol.io/r/api/article/5d8cbdef03f7410018856adf?ref=5d8a4524783fbd00182397db"
        },
        ...
    ]
}
```

## Contributors
[Raji Navarro](https://github.com/rajinavarro)</br>
[Lucas Torres](https://github.com/lucastorress)</br>
[Albert Queiroz](https://github.com/AlbertQueiroz)

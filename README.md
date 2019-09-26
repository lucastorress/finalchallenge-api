Apple Foundation - FinalChallenge API
=========================

Python API developed using Flask framework during process of Apple Foundation's class. Our team is composed by Raji, Albert and Lucas Torres. This API is used by mobile application developed in Swift and it's like a middleware.

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
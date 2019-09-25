from flask import jsonify
from api import app

import logging as logger
from api.controllers import responseListOfCoins as request_quotation_price

response = request_quotation_price.RESPONSE


@app.route('/api/v1/ranklist', methods=['GET'])
def RankList():
    logger.debug("Inside the get method of RankList")
    return jsonify({
        'ranklist': response
    }), 200

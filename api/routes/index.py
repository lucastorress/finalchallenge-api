from flask import jsonify
from api import app

import logging as logger


@app.route('/api/v1', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    logger.debug("Inside the get method of index")
    response = {
        'message': 'API is ready for use!',
        'url': [
            '/api/v1/simulation/<string:asset_id_base>/<int:value_base>/<string:buy_date>/<string:sell_date>',
            '/api/v1/simulation/',
            '/api/v1/simulationlist/',
            '/api/v1/ranklist',
        ]
        }
    return jsonify(response), 200

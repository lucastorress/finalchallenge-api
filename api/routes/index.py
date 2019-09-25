from flask import jsonify
from api import app

import logging as logger


@app.route('/api/v1', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    logger.debug("Inside the get method of index")
    response = {
        'message': 'API is ready for use!'
        }
    return jsonify(response), 200

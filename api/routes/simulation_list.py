from flask import jsonify
from api import app

import logging as logger
from api.controllers import responseListOfCoinsSimulation as request_simulation_list_coins

response = request_simulation_list_coins.response_list()


@app.route('/api/v1/simulationlist/', methods=['GET'])
def simulation_list():
    logger.debug("Inside the get method of Simulation List")
    http_code = 200

    return jsonify({
        'simulationlist': response
    }), http_code

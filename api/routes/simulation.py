from flask import jsonify
from api import app

import logging as logger
from api.controllers import requestRegressiveSimulation as request_simulation


@app.route('/api/v1/simulation', methods=['GET'])
@app.route(
    '/api/v1/simulation/<string:asset_id_base>/<string:asset_id_quote>/<int:value_base>/<string:buy_date>/<string:sell_date>',
    methods=['GET'])
def Simulation(asset_id_base=None, asset_id_quote=None, value_base=None,
               buy_date=None, sell_date=None):

    logger.debug("Inside the get method of Simulation")

    if asset_id_base is None or asset_id_quote is None or value_base is None\
       or buy_date is None or sell_date is None:
        response = {
            'message': 'Fill in the fields correctly!'
        }
        http_code = 400
    else:
        response = request_simulation(asset=f'{asset_id_base}/{asset_id_quote}',
                                      baseInvestiment=value_base,
                                      initialDate=buy_date,
                                      finalDate=sell_date)

    return jsonify(response), http_code

from flask_restful import Resource
from .core import request
import logging as logger


class RegressiveSimulator(Resource):
    def get(self, asset_id_base, asset_id_quote, value_base, time=False):
        logger.debug("Inside the get method of RegressiveSimulator")
        response = request(asset=f'{asset_id_base}/{asset_id_quote}',
                           baseInvestiment=value_base,
                           initialDate=time)
        return response, 200

    def post(self, asset_id_base, asset_id_quote, value_base, time=False):
        logger.debug("Inside the post method of RegressiveSimulation")
        return {
            "message": "This post method was not implemented."
        }, 200

    def put(self, asset_id_base, asset_id_quote, value_base, time=False):
        logger.debug("Inside the put method of RegressiveSimulation")
        return {
            "message": "This put method was not implemented."
        }, 200

    def delete(self, asset_id_base, asset_id_quote, value_base, time=False):

        logger.debug("Inside the delete method of RegressiveSimulation")
        return {
            "message": "This delete method was not implemented."
        }, 200

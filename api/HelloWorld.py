from flask_restful import Resource
import logging as logger


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

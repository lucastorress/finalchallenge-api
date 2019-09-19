from flask_restful import Api
from app import app
from .RegressiveSimulation import RegressiveSimulator
from .HelloWorld import HelloWorld

restServerInstance = Api(app)

restServerInstance.add_resource(HelloWorld, '/')
restServerInstance.add_resource(
    RegressiveSimulator,
    "/api/v1/regressivesimulation/<string:asset_id_base>/<string:asset_id_quote>/<int:value_base>/<string:time>"
)

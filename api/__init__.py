from flask_restful import Api
from app import app as instanceOfApp
from .RegressiveSimulation import RegressiveSimulator
from .HelloWorld import HelloWorld

restServerInstance = Api(instanceOfApp)

restServerInstance.add_resource(HelloWorld, '/')
restServerInstance.add_resource(
    RegressiveSimulator,
    "/api/v1/regressivesimulation/<int:value_base>"
)
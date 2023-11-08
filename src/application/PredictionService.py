from domain.services.IPredictionService import IPredictionService
from domain.entities.PredictionRequest import PredictionRequest
from infrastructure.TorchServeClient import TorchServeClient

class PredictionService(IPredictionService):
    def __init__(self, torchserve_client: TorchServeClient):
        self.torchserve_client = torchserve_client

    def predict(self, request: PredictionRequest):
        # Add business logic
        prediction = self.torchserve_client.predict(request)
        return prediction

from abc import ABC, abstractmethod
from domain.entities.PredictionRequest import PredictionRequest

class IPredictionService(ABC):
    @abstractmethod
    def predict(self, prediction_request: PredictionRequest):
        pass
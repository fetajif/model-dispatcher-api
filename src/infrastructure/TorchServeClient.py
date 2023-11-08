import requests
from domain.entities.PredictionRequest import PredictionRequest
from domain.entities.PredictionResult import PredictionResult
from domain.exceptions.ErrorResponse import ErrorResponse
class TorchServeClient:
    
    def get_torchserve_endpoint(self, prediction_request: PredictionRequest):
        return f"{prediction_request.http_protocol}://{prediction_request.host}:{prediction_request.port}/predictions/{prediction_request.model_name}"

    def predict(self, prediction_request: PredictionRequest):
        try:
            endpoint = self.get_torchserve_endpoint(prediction_request)
            input_data = {
                "max-model-page": prediction_request.max_model_page,
                "postprocessingsteps": prediction_request.postprocessingsteps,
                "input-media-type": prediction_request.input_media_type
            }

            response = requests.post(endpoint, json=input_data)
            response_data = response.json()
            result = PredictionResult(prediction_value=response_data, model_name=prediction_request.model_name)
            return result
        except Exception as e:
            print(e)
            return ErrorResponse(status=404, msg="Error communicating with TorchServe")

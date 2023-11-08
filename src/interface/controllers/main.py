from application.PredictionService import PredictionService
from domain.entities.PredictionRequest import PredictionRequest
from domain.entities.PredictionResult import PredictionResult
from infrastructure.TorchServeClient import TorchServeClient
from fastapi import FastAPI, Depends
import requests
import uvicorn
# Enable Swagger documentation
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import OpenAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

def get_prediction_service():
    torch_serve_client = TorchServeClient()
    prediction_service = PredictionService(torch_serve_client)
    return prediction_service

# configuring swagger for fast api
async def custom_openapi():
    openapi_schema = app.openapi()
    openapi_schema["info"]["title"] = "Model Dispatcher"
    return JSONResponse(content=openapi_schema)

@app.get("/openapi.json", response_model=OpenAPI, include_in_schema=False)
async def get_open_api_endpoint():
    return app.openapi()

@app.get("/docs", include_in_schema=False)
async def get_swagger_ui_html(request: Request):
    return get_swagger_ui_html(
        request=request,
        title="Model Dispatcher",
        openapi_url="/openapi.json",
    )

############

@app.post("/dispatch_model/")
async def predict(request: PredictionRequest, prediction_service = Depends(get_prediction_service)):
    prediction = prediction_service.predict(request)
    return prediction



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

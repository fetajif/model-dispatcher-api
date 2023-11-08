from pydantic import BaseModel

class PredictionRequest(BaseModel):
    host: str
    port: str
    http_protocol: str
    smarttool: str
    max_model_page: int
    postprocessingsteps: str
    input_media_type: str
    username: str
    password: str
    token: str
    model_name: str
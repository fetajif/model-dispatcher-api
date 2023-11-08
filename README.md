# Model Dispatcher API using FastAPI
The Model Dispatcher is a FastAPI-based web application that serves as a middleware for communicating with TorchServe, a model serving framework. This documentation describes the structure, endpoints, and usage of the Model Dispatcher.
## Instructions on how to build and run the dockerfile
docker build -t model-dispatcher .

docker run -dp 8000:8000 model-dispatcher

## App structure and architecture

The application follows the principles of Onion Architecture, with each layer having a specific purpose:
 - **Application Layer**: /application, this layer contains the **PredictionService** responsible for implementing the prediction service and business logic for communicating with TorchServe. This layer represents the core application functionality.
 - **Domain Layer**: /domain, this layer encapsulates the core data models, such as PredictionRequest and PredictionResult, and the ErrorResponse model for handling error responses. It defines the entities and exceptions used in the application.
 - **Infrastructure Layer**: /infrastructure, this layer contains the TorchServeClient, which is responsible for communication with external services, such as TorchServe. It deals with the technical aspects of interaction.
 - **Interface Layer**: /interface,  The main.py file defines FastAPI routes and acts as the application's entry point. It is responsible for handling HTTP requests and responses, as well as routing them to the appropriate application services.
 - **Docker Configuration**: The Dockerfile at the root of the project specifies the container configuration for deployment.
 - The requirements.txt file lists the required Python packages for the application.

## Swagger Documentation

You can access the Swagger documentation for the Model Dispatcher API by navigating to /docs. 

URL: localhost:8000/docs

## Endpoints

<h3> POST /dispatch_model  </h3>
 - request: A JSON object representing a PredictionRequest.
 
   ![image](https://github.com/fetajif/model-dispatcher-api/assets/74158530/f3d60932-83b9-4784-adde-fc2862f15784)

 - Description: This endpoint sends a prediction request to TorchServe and returns the prediction result. It handles the communication with TorchServe and passes the request data to the TorchServeClient. Any errors in the process will be captured and returned as an ErrorResponse object.

## Communication with TorchServe
The Model Dispatcher follows the Onion Architecture principles:

 - Application Layer: The PredictionService within this layer contains the business logic for predicting models and orchestrating the interaction with TorchServe.

 - Domain Layer: This layer defines the data models, such as PredictionRequest, PredictionResult, and ErrorResponse, ensuring that they represent the core entities and exceptions used in the application.

 - Infrastructure Layer: The TorchServeClient located in this layer is responsible for making HTTP requests to TorchServe endpoints. As seen in examples on the torchserve api docs the url for the request is built similar to https://pytorch.org/serve/inference_api.html#predictions-api, so: {http-protocol}://{host}:{port}/predictions/{model_name}


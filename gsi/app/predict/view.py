from typing import Dict, Union

from fastapi.responses import JSONResponse

from gsi.app.predict.controller import predictor
from gsi.app.predict.model import InputPredict
from log_manager import log
from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/predict",
    summary="It returns the prediction",
    response_description="It returns the prediction",
)
def predict(input_data: InputPredict):
    """
    This endpoint returns the prediction.
    Returns:
        It returns a dictionary containing the prediction.
    """
    log.logger.info(f'endpoint /predict called with parameter {input_data}')
    # # try:
    log.logger.info(f'trying to predict variables {input_data}')
    prediction = predictor(input_data)
    log.logger.info(f'The prediction for the variables {input_data} is {prediction}')
    return prediction

    # except FileNotFoundError:
    #     log.logger.error(f'No model found! Variables {input_data}')
    #     return JSONResponse(status_code=404,
    #                         content="I am sorry, the model is not trained yet, please call the endpoint /train first!")



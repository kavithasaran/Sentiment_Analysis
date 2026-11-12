from fastapi import APIRouter, HTTPException, Request

from app.schemas.prediction_schema import PredictionRequest, PredictionResponse
from app.services.prediction_service import predict_sentiment

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(request: Request, data: PredictionRequest):

    # Combine heading and review
    combined_review = f"{data.heading} {data.review}"

    try:
        sentiment = predict_sentiment(
            combined_review, data.model_name, request.app.state.models
        )

        return PredictionResponse(
            heading=data.heading,
            review=data.review,
            selected_model=data.model_name,
            sentiment=sentiment,
        )

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

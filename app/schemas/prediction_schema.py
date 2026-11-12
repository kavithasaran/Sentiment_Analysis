
from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    heading: str = Field(..., min_length=1)
    review: str = Field(..., min_length=1)
    model_name: str = Field(...)


class PredictionResponse(BaseModel):
    heading: str
    review: str
    selected_model: str
    sentiment: str

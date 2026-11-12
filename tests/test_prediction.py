import pytest

from app.services.prediction_service import predict_sentiment


def test_invalid_model_selection():
    with pytest.raises(ValueError, match="Invalid model selection"):
        predict_sentiment(
            "This is a good product", "invalid_model", (None, None, None, None)
        )

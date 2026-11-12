from fastapi.testclient import TestClient

from app.main import app


def test_home_page():
    with TestClient(app) as client:
        response = client.get("/")

        assert response.status_code == 200
        assert "Sentiment Analysis WebApp" in response.text


def test_prediction_invalid_model():
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={
                "heading": "Great product",
                "review": "I really liked this product.",
                "model_name": "invalid_model",
            },
        )

        assert response.status_code == 400
        assert response.json()["detail"] == "Invalid model selection."

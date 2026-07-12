from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "Running"


def test_route():
    response = client.post(
        "/route",
        json={
            "prompt": "What is Artificial Intelligence?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "model" in data
    assert "response" in data
    assert "confidence" in data
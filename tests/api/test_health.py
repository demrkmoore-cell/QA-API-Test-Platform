import requests


BASE_URL = "http://127.0.0.1:8000"


def test_health_endpoint():
    response = requests.get(f"{BASE_URL}/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

import requests


BASE_URL = "http://127.0.0.1:8000"


def test_get_products():
    response = requests.get(f"{BASE_URL}/api/products/")

    assert response.status_code == 200

    products = response.json()

    assert isinstance(products, list)
    assert len(products) >= 1

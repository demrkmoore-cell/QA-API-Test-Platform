import requests


BASE_URL = "http://127.0.0.1:8000"


def test_create_product():
    payload = {
        "name": "Automated QA Product",
        "description": "Created by Pytest",
        "price": 49.99,
        "stock_quantity": 25,
    }

    response = requests.post(f"{BASE_URL}/api/products/", json=payload)

    assert response.status_code == 201

    product = response.json()

    assert product["name"] == "Automated QA Product"
    assert product["price"] == 49.99
    assert product["stock_quantity"] == 25

import requests


BASE_URL = "http://127.0.0.1:8000"


def test_create_product_rejects_zero_price():
    payload = {
        "name": "Invalid Price Product",
        "description": "Negative API test",
        "price": 0,
        "stock_quantity": 5,
    }

    response = requests.post(f"{BASE_URL}/api/products/", json=payload)

    assert response.status_code == 422


def test_create_product_rejects_missing_name():
    payload = {
        "price": 25.00,
        "stock_quantity": 5,
    }

    response = requests.post(f"{BASE_URL}/api/products/", json=payload)

    assert response.status_code == 422


def test_create_product_rejects_negative_stock():
    payload = {
        "name": "Invalid Stock Product",
        "description": "Negative API test",
        "price": 25.00,
        "stock_quantity": -1,
    }

    response = requests.post(f"{BASE_URL}/api/products/", json=payload)

    assert response.status_code == 422


def test_create_product_accepts_zero_stock():
    payload = {
        "name": "Zero Stock Product",
        "description": "Boundary API test",
        "price": 25.00,
        "stock_quantity": 0,
    }

    response = requests.post(f"{BASE_URL}/api/products/", json=payload)

    assert response.status_code == 201

    product = response.json()

    assert product["stock_quantity"] == 0


def test_create_product_rejects_missing_price():
    payload = {
        "name": "Missing Price Product",
        "stock_quantity": 5,
    }

    response = requests.post(f"{BASE_URL}/api/products/", json=payload)

    assert response.status_code == 422

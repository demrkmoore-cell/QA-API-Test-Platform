import requests


BASE_URL = "http://127.0.0.1:8000"


def test_get_products():
    response = requests.get(f"{BASE_URL}/api/products/")

    assert response.status_code == 200

    products = response.json()

    assert isinstance(products, list)
    assert len(products) >= 1


def test_get_product_by_id():
    response = requests.get("http://127.0.0.1:8000/api/products/13")

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == 13
    assert product["name"] == "Postman QA Product"
    assert product["price"] == 79.99
    assert product["stock_quantity"] == 15

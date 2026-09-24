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
    assert product["name"]
    assert product["price"] > 0
    assert product["stock_quantity"] >= 0


def test_update_product():
    response = requests.put(
        "http://127.0.0.1:8000/api/products/13",
        json={
            "name": "Automated QA Product",
            "description": "Updated through automated API testing",
            "price": 99.99,
            "stock_quantity": 25,
        },
    )

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == 13
    assert product["name"] == "Automated QA Product"
    assert product["price"] == 99.99
    assert product["stock_quantity"] == 25


def test_update_product_not_found():
    response = requests.put(
        f"{BASE_URL}/api/products/999999",
        json={
            "name": "Missing Product",
            "description": "Should not exist",
            "price": 10.00,
            "stock_quantity": 1,
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

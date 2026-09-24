import requests


BASE_URL = "http://127.0.0.1:8000"


def test_get_products():
    response = requests.get(f"{BASE_URL}/api/products/")

    assert response.status_code == 200

    products = response.json()

    assert isinstance(products, list)
    assert len(products) >= 1


def test_get_product_by_id():
    create_response = requests.post(
        f"{BASE_URL}/api/products/",
        json={
            "name": "GET By ID Test Product",
            "description": "Created for GET by ID testing",
            "price": 35.00,
            "stock_quantity": 8,
        },
    )

    assert create_response.status_code == 201

    product_id = create_response.json()["id"]

    response = requests.get(f"{BASE_URL}/api/products/{product_id}")

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == product_id
    assert product["name"] == "GET By ID Test Product"
    assert product["price"] == 35.00
    assert product["stock_quantity"] == 8


def test_update_product():
    create_response = requests.post(
        f"{BASE_URL}/api/products/",
        json={
            "name": "Update Test Product",
            "description": "Created for update testing",
            "price": 45.00,
            "stock_quantity": 10,
        },
    )

    assert create_response.status_code == 201

    product_id = create_response.json()["id"]

    response = requests.put(
        f"{BASE_URL}/api/products/{product_id}",
        json={
            "name": "Updated QA Product",
            "description": "Updated through automated API testing",
            "price": 99.99,
            "stock_quantity": 25,
        },
    )

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == product_id
    assert product["name"] == "Updated QA Product"
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


def test_delete_product():
    create_response = requests.post(
        f"{BASE_URL}/api/products/",
        json={
            "name": "Delete Test Product",
            "description": "Created for DELETE API testing",
            "price": 25.00,
            "stock_quantity": 5,
        },
    )

    assert create_response.status_code == 201

    product_id = create_response.json()["id"]

    delete_response = requests.delete(f"{BASE_URL}/api/products/{product_id}")

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Product deleted successfully"

    get_response = requests.get(f"{BASE_URL}/api/products/{product_id}")

    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Product not found"


def test_delete_product_not_found():
    response = requests.delete(f"{BASE_URL}/api/products/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

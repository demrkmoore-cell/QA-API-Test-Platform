import requests

BASE_URL = "http://127.0.0.1:8000"
REQUEST_TIMEOUT = 10


def test_list_products_includes_created_product(product_factory):
    payload = {
        "name": "List Endpoint QA Product",
        "description": "Verify product listing",
        "price": 18.25,
        "stock_quantity": 4,
    }
    created = product_factory(payload)
    assert created.status_code == 201
    product_id = created.json()["id"]

    response = requests.get(f"{BASE_URL}/api/products/", timeout=REQUEST_TIMEOUT)

    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)
    assert any(product["id"] == product_id for product in products)


def test_get_product_by_id_returns_created_product(product_factory):
    payload = {
        "name": "Get Endpoint QA Product",
        "description": "Verify product lookup",
        "price": 21.50,
        "stock_quantity": 6,
    }
    created = product_factory(payload)
    assert created.status_code == 201
    product_id = created.json()["id"]

    response = requests.get(
        f"{BASE_URL}/api/products/{product_id}", timeout=REQUEST_TIMEOUT
    )

    assert response.status_code == 200
    product = response.json()
    assert product["id"] == product_id
    assert product["name"] == payload["name"]
    assert float(product["price"]) == payload["price"]


def test_update_product_persists_changed_values(product_factory):
    payload = {
        "name": "Product Before Update",
        "description": "Initial value",
        "price": 10.00,
        "stock_quantity": 2,
    }
    created = product_factory(payload)
    assert created.status_code == 201
    product_id = created.json()["id"]

    updated_payload = {
        "name": "Product After Update",
        "description": "Updated value",
        "price": 12.75,
        "stock_quantity": 8,
    }
    response = requests.put(
        f"{BASE_URL}/api/products/{product_id}",
        json=updated_payload,
        timeout=REQUEST_TIMEOUT,
    )

    assert response.status_code == 200
    product = response.json()
    assert product["id"] == product_id
    assert product["name"] == updated_payload["name"]
    assert product["description"] == updated_payload["description"]
    assert float(product["price"]) == updated_payload["price"]
    assert product["stock_quantity"] == updated_payload["stock_quantity"]


def test_delete_product_removes_it_from_api(product_factory):
    payload = {
        "name": "Delete Endpoint QA Product",
        "description": "Verify product deletion",
        "price": 14.00,
        "stock_quantity": 3,
    }
    created = product_factory(payload)
    assert created.status_code == 201
    product_id = created.json()["id"]

    deleted = requests.delete(
        f"{BASE_URL}/api/products/{product_id}", timeout=REQUEST_TIMEOUT
    )

    assert deleted.status_code == 200
    assert deleted.json() == {"message": "Product deleted successfully"}

    lookup = requests.get(
        f"{BASE_URL}/api/products/{product_id}", timeout=REQUEST_TIMEOUT
    )
    assert lookup.status_code == 404
    assert lookup.json()["detail"] == "Product not found"


def test_get_unknown_product_returns_404():
    response = requests.get(f"{BASE_URL}/api/products/2147483647", timeout=REQUEST_TIMEOUT)

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

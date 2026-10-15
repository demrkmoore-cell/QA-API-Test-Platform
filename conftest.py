import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture
def product_factory():
    created_product_ids = []

    def create_product(payload):
        response = requests.post(
            f"{BASE_URL}/api/products/",
            json=payload,
            timeout=10,
        )

        if response.status_code == 201:
            created_product_ids.append(response.json()["id"])

        return response

    yield create_product

    for product_id in reversed(created_product_ids):
        response = requests.delete(
            f"{BASE_URL}/api/products/{product_id}",
            timeout=10,
        )
        assert response.status_code in (200, 204, 404)

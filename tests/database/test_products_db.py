import sys
from pathlib import Path

import requests
from sqlalchemy import text

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.database import engine


def test_api_created_product_is_persisted(product_factory):
    payload = {
        "name": "Database Persistence Test",
        "description": "Verify API-created product is stored in PostgreSQL",
        "price": 42.50,
        "stock_quantity": 7,
    }

    response = product_factory(payload)
    assert response.status_code == 201
    product_id = response.json()["id"]

    with engine.connect() as connection:
        product = connection.execute(
            text("""
                SELECT id, name, price, stock_quantity
                FROM products
                WHERE id = :product_id
            """),
            {"product_id": product_id},
        ).mappings().first()

    assert product is not None
    assert product["id"] == product_id
    assert product["name"] == payload["name"]
    assert float(product["price"]) == payload["price"]
    assert product["stock_quantity"] == payload["stock_quantity"]


def test_api_update_is_persisted_in_database(product_factory):
    payload = {
        "name": "Database Update Test",
        "description": "Verify updated product values are stored",
        "price": 15.00,
        "stock_quantity": 2,
    }

    create_response = product_factory(payload)
    assert create_response.status_code == 201
    product_id = create_response.json()["id"]

    updated_payload = {
        "name": "Database Update Verified",
        "description": "Updated through the product API",
        "price": 28.75,
        "stock_quantity": 9,
    }

    update_response = requests.put(
        f"http://127.0.0.1:8000/api/products/{product_id}",
        json=updated_payload,
        timeout=10,
    )
    assert update_response.status_code == 200

    with engine.connect() as connection:
        product = connection.execute(
            text("""
                SELECT id, name, price, stock_quantity
                FROM products
                WHERE id = :product_id
            """),
            {"product_id": product_id},
        ).mappings().first()

    assert product is not None
    assert product["id"] == product_id
    assert product["name"] == updated_payload["name"]
    assert float(product["price"]) == updated_payload["price"]
    assert product["stock_quantity"] == updated_payload["stock_quantity"]

def test_create_product(product_factory):
    payload = {
        "name": "Automated QA Product",
        "description": "Created by Pytest",
        "price": 49.99,
        "stock_quantity": 25,
    }

    response = product_factory(payload)

    assert response.status_code == 201

    product = response.json()

    assert product["name"] == "Automated QA Product"
    assert float(product["price"]) == 49.99
    assert product["stock_quantity"] == 25

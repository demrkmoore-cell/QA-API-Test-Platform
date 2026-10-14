import requests


BASE_URL = "http://127.0.0.1:8000"


def test_products_page_escapes_html_in_product_name():
    malicious_name = '<script>alert("qa-test")</script>'
    create_response = requests.post(
        f"{BASE_URL}/api/products/",
        json={
            "name": malicious_name,
            "description": "HTML escaping regression test",
            "price": 12.34,
            "stock_quantity": 1,
        },
    )

    assert create_response.status_code == 201
    product_id = create_response.json()["id"]

    try:
        page_response = requests.get(f"{BASE_URL}/products")
        assert page_response.status_code == 200
        assert "&lt;script&gt;alert(&quot;qa-test&quot;)&lt;/script&gt;" in page_response.text
        assert malicious_name not in page_response.text
    finally:
        delete_response = requests.delete(f"{BASE_URL}/api/products/{product_id}")
        assert delete_response.status_code == 200

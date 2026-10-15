import requests

BASE_URL = "http://127.0.0.1:8000"
REQUEST_TIMEOUT = 10


def test_product_name_is_escaped_in_html(product_factory):
    product_name = '<script>alert("qa-test")</script>'

    create_response = product_factory({
        "name": product_name,
        "description": "HTML escaping regression test",
        "price": 12.50,
        "stock_quantity": 1,
    })

    assert create_response.status_code == 201

    page_response = requests.get(
        f"{BASE_URL}/products",
        timeout=REQUEST_TIMEOUT,
    )
    assert page_response.status_code == 200

    html = page_response.text
    assert '&lt;script&gt;alert(&quot;qa-test&quot;)&lt;/script&gt;' in html
    assert product_name not in html

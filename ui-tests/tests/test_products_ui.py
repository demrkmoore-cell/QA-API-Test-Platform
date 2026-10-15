import sys
from pathlib import Path

from playwright.sync_api import Page, expect

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pages.products_page import ProductsPage


def test_products_page_loads(page: Page):
    products_page = ProductsPage(page)

    products_page.open()

    expect(products_page.page_heading).to_be_visible()
    expect(products_page.products_heading).to_be_visible()
    expect(products_page.products_table).to_be_visible()


def test_products_page_displays_product_data(page: Page, product_factory):
    payload = {
        "name": "Playwright UI Test Product",
        "description": "Created for browser UI verification",
        "price": 63.25,
        "stock_quantity": 11,
    }

    response = product_factory(payload)
    assert response.status_code == 201

    products_page = ProductsPage(page)
    products_page.open()

    expect(products_page.products_table).to_contain_text(
        "Playwright UI Test Product"
    )
    expect(products_page.products_table).to_contain_text("63.25")
    expect(products_page.products_table).to_contain_text("11")

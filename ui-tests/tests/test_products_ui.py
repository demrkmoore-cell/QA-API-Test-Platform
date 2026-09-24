from playwright.sync_api import Page, expect


def test_products_page_loads(page: Page):
    page.goto("http://127.0.0.1:8000/products")

    expect(page).to_have_title("QA API Test Platform - Products")
    expect(page.get_by_role("heading", name="QA API Test Platform")).to_be_visible()
    expect(page.get_by_role("heading", name="Products")).to_be_visible()
    expect(page.get_by_role("table")).to_be_visible()


def test_products_page_displays_product_data(page: Page):
    page.goto("http://127.0.0.1:8000/products")

    product_table = page.get_by_role("table")
    expect(product_table).to_contain_text("Postman QA Product")
    expect(product_table).to_contain_text("79.99")
    expect(product_table).to_contain_text("15")

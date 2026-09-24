from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.products_table = page.get_by_role("table")
        self.page_heading = page.get_by_role(
            "heading", name="QA API Test Platform"
        )
        self.products_heading = page.get_by_role(
            "heading", name="Products"
        )

    def open(self):
        self.page.goto("http://127.0.0.1:8000/products")

    def is_loaded(self):
        return (
            self.page_heading.is_visible()
            and self.products_heading.is_visible()
            and self.products_table.is_visible()
        )

    def table_contains(self, text: str):
        return self.products_table.get_by_text(text).is_visible()

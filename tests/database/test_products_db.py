import sys
from pathlib import Path

from sqlalchemy import text

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.database import engine


def test_products_table_contains_data():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT COUNT(*) FROM products")
        )
        product_count = result.scalar()

    assert product_count > 0

def test_latest_product_has_expected_fields():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT id, name, price, stock_quantity
                FROM products
                ORDER BY id DESC
                LIMIT 1
            """)
        )
        product = result.mappings().first()

    assert product is not None
    assert product["id"] is not None
    assert product["name"]
    assert product["price"] > 0
    assert product["stock_quantity"] >= 0

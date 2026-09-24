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

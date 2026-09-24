from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import Product

router = APIRouter(tags=["UI"])


@router.get("/products", response_class=HTMLResponse)
def products_page(db: Session = Depends(get_db)):
    products = db.query(Product).order_by(Product.id).all()

    product_rows = ""

    for product in products:
        product_rows += f"""
        <tr>
            <td>{product.id}</td>
            <td>{product.name}</td>
            <td>${product.price}</td>
            <td>{product.stock_quantity}</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>QA API Test Platform - Products</title>
    </head>
    <body>
        <h1>QA API Test Platform</h1>
        <h2>Products</h2>

        <table border="1">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Stock</th>
                </tr>
            </thead>
            <tbody>
                {product_rows}
            </tbody>
        </table>
    </body>
    </html>
    """

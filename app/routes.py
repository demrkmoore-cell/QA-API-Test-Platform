from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import Product
from app.schemas import ProductCreate, ProductUpdate

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock_quantity=product.stock_quantity,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.put("/{product_id}")
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
):
    existing_product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.stock_quantity = product.stock_quantity

    db.commit()
    db.refresh(existing_product)

    return existing_product


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    existing_product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(existing_product)
    db.commit()

    return {"message": "Product deleted successfully"}

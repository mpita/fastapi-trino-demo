from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from app.models import ProductsList, Products
from sqlmodel import select, func, desc

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=ProductsList)
async def list_products(
    session: SessionDep,
    skip: int = 0,
    limit: int = 100,
) -> ProductsList:
    count_query = select(func.count()).select_from(Products)
    count = session.exec(count_query).one()

    query = (
        select(Products)
        .order_by(desc(Products.manufacture_date), desc(Products.name))
        .offset(skip)
        .limit(limit)
    )
    products = session.exec(query).all()
    return ProductsList(data=products, count=count)

@router.get("/{product_id}", response_model=Products)
async def read_product(
    product_id: int,
    session: SessionDep,
) -> Products:
    product = session.get(Products, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
from fastapi import APIRouter
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
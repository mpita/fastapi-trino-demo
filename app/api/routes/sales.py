from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from app.models import SalesList, Sales, SaleDetail
from sqlmodel import select, func, desc
from sqlalchemy.orm import selectinload

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.get("/", response_model=SalesList)
async def list_sales(
    session: SessionDep,
    skip: int = 0,
    limit: int = 100,
) -> SalesList:
    count_query = select(func.count()).select_from(Sales)
    count = session.exec(count_query).one()

    query = (
        select(Sales)
        .order_by(desc(Sales.sale_timestamp))
        .offset(skip)
        .limit(limit)
    )
    sales = session.exec(query).all()
    return SalesList(data=sales, count=count)


@router.get("/{sale_id}", response_model=SaleDetail)
async def read_sale(
    sale_id: int,
    session: SessionDep,
) -> SaleDetail:
    query = (
        select(Sales)
        .options(selectinload(Sales.customer), selectinload(Sales.product))
        .where(Sales.sale_id == sale_id)
    )
    sale = session.exec(query).first()
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale
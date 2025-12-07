from fastapi import APIRouter
from app.api.deps import SessionDep
from app.models import SalesList, Sales
from sqlmodel import select, func, desc

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
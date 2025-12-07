from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from app.models import CustomersList, Customers
from sqlmodel import select, func, desc

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/", response_model=CustomersList)
async def list_customers(
    session: SessionDep,
    skip: int = 0,
    limit: int = 100,
) -> CustomersList:
    count_query = select(func.count()).select_from(Customers)
    count = session.exec(count_query).one()

    query = (
        select(Customers)
        .order_by(Customers.first_name, Customers.last_name)
        .offset(skip)
        .limit(limit)
    )
    customers = session.exec(query).all()
    return CustomersList(data=customers, count=count)


@router.get("/{customer_id}", response_model=Customers)
async def read_customer(
    customer_id: int,
    session: SessionDep,
) -> Customers:
    customer = session.get(Customers, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
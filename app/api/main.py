from fastapi import APIRouter

from app.api.routes import products, customers, sales

routers = APIRouter()
routers.include_router(products.router)
routers.include_router(customers.router)
routers.include_router(sales.router)
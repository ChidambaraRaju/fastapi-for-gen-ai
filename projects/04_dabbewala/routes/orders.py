from fastapi import APIRouter, Depends, HTTPException, Query
from database import get_session
from models import Order, OrderCreate, OrderUpdate, StatusLog, OrderStatus
from sqlmodel import Session, select
from datetime import datetime


router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=Order)
def create_order(order: OrderCreate, session: Session = Depends(get_session)):
    db_order = Order(**order.model_dump())
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order

@router.get("/", response_model=list[Order])
def list_orders(
    status: OrderStatus | None = Query(None, description="Filter by order status"),
    created_date: str | None = Query(None, description="Filter by creation date (YYYY-MM-DD)"),
    skip: int = Query(0, ge=0, description="Number of orders to skip/offset"),
    limit: int = Query(10, ge=1, le=50, description="Max orders to return"),
    session: Session = Depends(get_session)
):
    query = select(Order)
    if status:
        query = query.where(Order.status == status)
    if created_date:
        start = datetime.combine(created_date, datetime.min.time())
        end = datetime.combine(created_date, datetime.max.time())
        query = query.where(Order.created_at.between(start, end))
    query = query.offset(skip).limit(limit)
    return session.exec(query).all()
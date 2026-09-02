from enum import Enum
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

# OrderStatus (Enum) -> preparing, picked_up, in_transit, delivered
class OrderStatus(str, Enum):
    PREPARING = "preparing"
    PICKED_UP = "picked_up"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"

# Database table for orders
class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_name: str
    delivery_address: str
    items: str
    status: OrderStatus = Field(default=OrderStatus.PREPARING)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

# Schema for creating a new order
class OrderCreate(SQLModel):
    customer_name: str
    delivery_address: str
    items: str

# Schema for updating an existing order
class OrderUpdate(SQLModel):
    status: Optional[OrderStatus]
    delivery_address: Optional[str]

# StatusLog
class StatusLog(SQLModel):
    order_id: int
    old_status: str
    new_status: str
    changed_at: datetime
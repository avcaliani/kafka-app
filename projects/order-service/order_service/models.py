from datetime import UTC, datetime
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, EmailStr, Field


class Order(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    customer_email: EmailStr
    items: list
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

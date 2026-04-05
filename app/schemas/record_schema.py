from pydantic import BaseModel, Field
from datetime import date
from typing import Literal, Optional


class RecordCreate(BaseModel):
    amount: float = Field(gt=0)
    type: Literal["income", "expense"]
    category: str
    date: date
    description: Optional[str] = None
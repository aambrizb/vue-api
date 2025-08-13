from sqlmodel import Field, Session, SQLModel
from pydantic import BaseModel

class Product(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str = Field(index=True)
  active: bool | None = Field(default=True, index=True)
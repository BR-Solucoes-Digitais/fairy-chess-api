from uuid import UUID, uuid4
from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default=uuid4(), primary_key=True, )
    usernaem: str = Field(index=True, nullable=False)
    password: str = Field(nullable=False)
    riot_id: str = Field(nullable=True)
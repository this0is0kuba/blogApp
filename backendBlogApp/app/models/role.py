from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from .user_role import UserRoleLink

if TYPE_CHECKING:
    from .user import User


class Role(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str

    users: list["User"] = Relationship(back_populates="roles", link_model=UserRoleLink)

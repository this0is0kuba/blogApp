from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .blog import Blog


class Category(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    name: str

    blogs: list["Blog"] = Relationship(back_populates="category")



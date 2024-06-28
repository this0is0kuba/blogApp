from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .blog_tag import BlogTagLink


class Tag(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str

    blog_links: list["BlogTagLink"] = Relationship(back_populates="tag")

from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from .blog_category import BlogCategoryLink

if TYPE_CHECKING:
    from .blog import Blog


class Category(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str

    blogs: list["Blog"] = Relationship(back_populates="categories", link_model=BlogCategoryLink)



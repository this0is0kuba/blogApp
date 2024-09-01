from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

from .user import UserPublic
from .category import Category

if TYPE_CHECKING:
    from .comment import Comment
    from .category import Category
    from .blog_tag import BlogTagLink


class BlogBase(SQLModel):
    title: str = Field(min_length=1, max_length=30)
    content: str = Field(min_length=1, max_length=10_000)
    creation_date: datetime

    author_id: int = Field(foreign_key="user.id")
    category_id: int = Field(foreign_key="category.id")


class Blog(BlogBase, table=True):
    id: int | None = Field(primary_key=True, default=None)

    author: "User" = Relationship(back_populates="blogs")
    comments: list["Comment"] = Relationship(back_populates="blog")
    category: "Category" = Relationship(back_populates="blogs")
    tag_links: list["BlogTagLink"] = Relationship(back_populates="blog")


class BlogCreate(BlogBase):
    pass


class BlogPublic(BlogBase):
    id: int


class BlogPublicWithAuthor(BlogPublic):
    author: "UserPublic"
    category: "Category"



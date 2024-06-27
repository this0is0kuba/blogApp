from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING
from .blog_category import BlogCategoryLink
from .blog_tag import BlogTagLink
from .user import UserPublic
from .comment import CommentPublic

if TYPE_CHECKING:
    from comment import Comment
    from category import Category


class BlogBase(SQLModel):
    title: str = Field(min_length=1, max_length=30)
    content: str = Field(min_length=1, max_length=10_000)
    creationDate: datetime

    authorId: int = Field(foreign_key="user.id")


class Blog(BlogBase, table=True):
    id: int | None = Field(primary_key=True, default=None)

    author: "User" = Relationship(back_populates="blogs")
    comments: list["Comment"] = Relationship(back_populates="blog")
    categories: list["Category"] = Relationship(back_populates="blogs", link_model=BlogCategoryLink)
    tagLinks: list["BlogTagLink"] = Relationship(back_populates="blog")


class BlogCreate(BlogBase):
    pass


class BlogPublic(BlogBase):
    id: int


class BlogPublicWithAuthorAndComments(BlogPublic):
    author: "UserPublic"
    comments: list["CommentPublic"]


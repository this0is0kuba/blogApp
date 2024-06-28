from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user import User
    from blog import Blog


class CommentBase(SQLModel):
    content: str
    creationDate: datetime

    author_id: int = Field(foreign_key="user.id")
    blog_id: int = Field(foreign_key="blog.id")


class Comment(CommentBase, table=True):
    id: int | None = Field(primary_key=True, default=None)

    author: "User" = Relationship(back_populates="comments")
    blog: "Blog" = Relationship(back_populates="blogs")


class CommentCreate(CommentBase):
    pass


class CommentPublic(CommentBase):
    id: int

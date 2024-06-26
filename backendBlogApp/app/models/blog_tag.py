from sqlmodel import SQLModel, Relationship, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .blog import Blog
    from .tag import Tag


class BlogTagLink(SQLModel, table=True):
    visible: bool = True

    blogId: int | None = Field(primary_key=True, foreign_key="blog.id", default=None)
    tagId: int | None = Field(primary_key=True, foreign_key="tag.id", default=None)
    blog: "Blog" = Relationship(back_populates="tagLinks")
    tag: "Tag" = Relationship(back_populates="blogLinks")

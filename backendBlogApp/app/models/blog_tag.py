from sqlmodel import SQLModel, Relationship, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .blog import Blog
    from .tag import Tag


class BlogTagLink(SQLModel, table=True):
    visible: bool = True

    blog_id: int | None = Field(primary_key=True, foreign_key="blog.id", default=None)
    tag_id: int | None = Field(primary_key=True, foreign_key="tag.id", default=None)
    blog: "Blog" = Relationship(back_populates="tag_links")
    tag: "Tag" = Relationship(back_populates="blog_links")

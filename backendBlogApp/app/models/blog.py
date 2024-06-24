from sqlmodel import SQLModel, Field
from datetime import datetime


class BlogBase(SQLModel):

    title: str = Field(min_length=1, max_length=30)
    content: str = Field(min_length=1, max_length=10_000)


class Blog(BlogBase, table=True):

    id: int | None = Field(primary_key=True, default=None)
    creationDate: datetime


class BlogCreate(BlogBase):
    pass


class BlogPublic(BlogBase):
    id: int
    creationDate: datetime





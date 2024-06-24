from datetime import datetime
from sqlmodel import SQLModel, Field


class CommentBase(SQLModel):
    content: str


class Comment(CommentBase, table=True):
    id: int | None = Field(primary_key=True, default=None)
    creationDate: datetime


class CommentCreate(CommentBase):
    pass


class CommentPublic(CommentBase):
    id: int
    creationDate: datetime

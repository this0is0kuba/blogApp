from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from .user_role import UserRoleLink
from .blog import BlogPublic

if TYPE_CHECKING:
    from .blog import Blog
    from .comment import Comment
    from .role import Role


class UserBase(SQLModel):
    email: str = Field(max_length=50, index=True, unique=True)
    username: str = Field(max_length=20, index=True, unique=True)
    disabled: bool = False


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    passwordHash: str

    blogs: list["Blog"] = Relationship(back_populates="author")
    comments: list["Comment"] = Relationship(back_populates="author")
    roles: list["Role"] = Relationship(back_populates="users", link_model=UserRoleLink)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=30)


class UserPublic(UserBase):
    id: int


class UserPublicWithBlogs(UserPublic):
    blogs: list["BlogPublic"]



from sqlmodel import SQLModel, Field


class UserRoleLink(SQLModel, table=True):
    userId: int | None = Field(primary_key=True, foreign_key="user.id", default=None)
    roleId: int | None = Field(primary_key=True, foreign_key="role.id", default=None)

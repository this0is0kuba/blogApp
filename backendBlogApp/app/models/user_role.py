from sqlmodel import SQLModel, Field


class UserRoleLink(SQLModel, table=True):
    user_id: int | None = Field(primary_key=True, foreign_key="user.id", default=None)
    role_id: int | None = Field(primary_key=True, foreign_key="role.id", default=None)

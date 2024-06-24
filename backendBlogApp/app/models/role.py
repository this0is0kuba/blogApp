from sqlmodel import SQLModel, Field


class Role(SQLModel, table=True):
    id: Field(primary_key=True)
    roleName: str

from sqlmodel import SQLModel, Field


class Category(SQLModel, table=True):

    id: int = Field(primary_key=True)
    name: str

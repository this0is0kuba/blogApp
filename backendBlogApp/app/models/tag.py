from sqlmodel import SQLModel, Field


class Tag(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str

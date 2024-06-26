from sqlmodel import SQLModel, Field


class BlogCategoryLink(SQLModel, table=True):
    blogId: int | None = Field(primary_key=True, foreign_key="blog.id", default=None)
    categoryId: int | None = Field(primary_key=True, foreign_key="category.id", default=None)

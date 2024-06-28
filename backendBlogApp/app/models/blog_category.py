from sqlmodel import SQLModel, Field


class BlogCategoryLink(SQLModel, table=True):
    blog_id: int | None = Field(primary_key=True, foreign_key="blog.id", default=None)
    category_id: int | None = Field(primary_key=True, foreign_key="category.id", default=None)

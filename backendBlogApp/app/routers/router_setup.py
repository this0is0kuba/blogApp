from fastapi import FastAPI
from .category_router import router as category_router
from .blog_router import router as blog_router


def set_up_routers(app: FastAPI):

    app.include_router(category_router)
    app.include_router(blog_router)

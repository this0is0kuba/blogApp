from fastapi import FastAPI
from .blog_router import router as blog_router


def set_up_routers(app: FastAPI):

    app.include_router(blog_router)

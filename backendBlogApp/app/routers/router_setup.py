from fastapi import FastAPI
from .blog_router import router as blog_router
from .security_router import router as security_router
from .comments_router import router as comment_router


def set_up_routers(app: FastAPI):

    app.include_router(blog_router)
    app.include_router(security_router)
    app.include_router(comment_router)

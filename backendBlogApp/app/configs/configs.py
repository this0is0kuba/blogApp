from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

origins = [
    "http://localhost:3000",
]


def set_origins(app: FastAPI):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

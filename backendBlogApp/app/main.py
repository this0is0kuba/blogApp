from fastapi import FastAPI
from database import create_db_and_tables, drop_database
from configs.configs import set_origins
from routers.router_setup import set_up_routers

app = FastAPI()
set_origins(app)
# set_up_routers(app)


@app.on_event("startup")
def on_startup():

    # drop_database()
    create_db_and_tables()

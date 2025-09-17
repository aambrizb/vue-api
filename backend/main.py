from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from globaltechia import routers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins     = ["*"],
    allow_credentials = True,
    allow_methods     = ["*"],
    allow_headers     = ["*"],
)

app.include_router(routers.router)

@app.get("/")
def read_root():
    return {"status": "ready"}

register_tortoise(
    app,
    db_url                 = "sqlite://db.sqlite3",  # Can be postgres, mysql, etc.
    modules                = {"models": ["globaltechia.base.models"]},
    generate_schemas       = True,  # Auto-create tables
    add_exception_handlers = True,
)
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

DATABASE_CONFIG = {
    "connections": {
        "default": "sqlite://db.sqlite3"
    },
    "apps": {
        "models": {
            "models": ["globaltechia.base.models"],
            "default_connection": "default",
        }
    },
}
@app.get("/")
def read_root():
    return {"status": "ready"}

register_tortoise(
    app,
    config                 = DATABASE_CONFIG,
    generate_schemas       = True,  # Auto-create tables
    add_exception_handlers = True,
)
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from base.models import User
import time
import json
import importlib
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins     = ["*"],
    allow_credentials = True,
    allow_methods     = ["*"],
    allow_headers     = ["*"],
)

@app.get("/")
def read_root():
    return {"status": "ready"}

@app.api_route("/api/{app}/{view}",methods=["GET", "POST","DELETE"])
async def get_view(app,view,request: Request):

  _fullpath = os.getcwd()
  _module   = None
  _view     = None

  if os.path.exists(f"{_fullpath}/{app}/views.py"):
    _module = importlib.import_module(f'{app}.views')
    if _module and hasattr(_module,view):
      _view = getattr(_module,view)

    # Verify, if exists model.
    if not _module or not _view:
      _module = importlib.import_module(f'{app}.models')
      if _module and hasattr(_module,view):
        _model = getattr(_module,view)

        if _model:
          payload = await request.json()
          try:
            obj = await _model.create(**payload)
            return {
              "status":200,
              "id":obj.id,
              "msg":"Successfull Operation"
            }
          except Exception as ex:
            return {
              "status": 404,
              "msg": str(ex)
            }

      try:
        response = _view(request)
        return response
      except Exception as ex:
        return {
          "status":404,
          "msg":str(ex)
        }

  return {
    "method" : request['method'],
    "app"    : app,
    "view"   : view
  }

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",  # Can be postgres, mysql, etc.
    modules={"models": ["base.models"]},
    generate_schemas=True,  # Auto-create tables
    add_exception_handlers=True,
)
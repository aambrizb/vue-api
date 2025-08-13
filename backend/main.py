from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
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

@app.api_route("/echo",methods=["GET", "POST"])
async def echo(request: Request):
  return {
    "method":request['method']
  }

@app.api_route("/api/{app}/{view}",methods=["GET", "POST","DELETE"])
async def create_update(app,view,request: Request):

  _fullpath = os.getcwd()

  if os.path.exists(f"{_fullpath}/{app}/views.py"):
    _module = importlib.import_module(f'{app}.views')
    if _module:
      _view = getattr(_module,view)

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


@app.get("/api/app/navbar")
def get_navbar():

  data = [
    {
      "name"       : "Administración",
      "icon_class" : "fa fa-cog"
    },
    {
      "name"       : "Ordenes",
      "to"         : "create",
      "app"        : "app",
      "view"       : "orden",
      "icon_class" : "fa fa-times"
    },
    {
      "name"       : "Almacen",
      "icon_class" : "fa fa-cog"
    },
    {
      "name"       : "Productos",
      "to"         : "create",
      "app"        : "app",
      "view"       : "producto",
      "icon_class" : "fa fa-slash"
    },
    {
      "name"       : "Personalizada",
      "to"         : "create",
      "app"        : "app",
      "view"       : "personalizada",
      "icon_class" : "fa fa-slash"
    },
    {
      "name"       : "Reportes",
      "icon_class" : "fa fa-list"
    },
    {
      "name"       : "Activaciones",
      "to"         : "reporte_activaciones",
      "app"        : "app",
      "view"       : "personalizada",
      "icon_class" : "fa fa-file"
    }]

  return data


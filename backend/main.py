from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

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
    return {"Hello": "World"}
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


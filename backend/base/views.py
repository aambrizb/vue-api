def navbar(request):

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

def create(request):
  if request['method'] == 'GET':
    pass
  elif request['method'] == 'POST':
    data = request.json()

  return {"ok":"holis"}
def navbar(request,id=None):

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

def jaja_list(request,id=None):
  return {"orale":"orale que loco"}
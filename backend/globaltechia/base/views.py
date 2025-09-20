from globaltechia.base.models import Navbar
from globaltechia.utils import getModel

async def navbar(request):

  data = await Navbar.filter(parent_id=None).values()

  for item in data:
    item['children'] = await Navbar.filter(
      parent_id=item['id']
    ).values()

  return data

async def login(request):
  from globaltechia.base.models import User

  code     = 404
  msg      = ""
  token    = None
  fullname = None

  data = await request.json()

  _username = data['username']
  _passwd   = data['password']

  obj = await User.filter(email=_username).last()

  if not obj:
    code = 404
    msg  = "Usuario no válido."
  else:
    code     = 200
    msg      = "Operación realizada con éxito"
    token    = "token"
    fullname = f"{obj.first_name} {obj.last_name} {obj.middle_name}"

  return {
    "status"   : code,
    "msg"      : msg,
    "token"    : token,
    "fullname" : fullname
  }

async def removeModel(request):
  data     = await request.json()

  _app   = data.get('app',None)
  _model = data.get('model',None)
  _id    = data.get('id', None)

  _model = getModel(_app,_model)
  if _model:

    try:
      obj = await _model.get(id=_id)
      await obj.delete()
    except Exception as ex:
      print(f"[removeModel] {ex}")

  params = {
    "code" : 200,
    "msg"  : "Operación realizada con éxito"
  }

  return params

async def addModel(request):
  data     = await request.json()

  _app   = data.get('app',None)
  _model = data.get('model',None)
  _data  = data.get('data', None)

  _model = getModel(_app, _model)
  if _model:

    try:
      await _model.create(**_data)
    except Exception as ex:
      print(f"[addModel] {ex}")

  params = {
    "code" : 200,
    "msg"  : "Operación realizada con éxito"
  }

  return params

async def getModelData(request):

  code     = 200
  msg      = "Operación realizada con éxito"

  data = await request.json()

  _app       = data.get('app', None)
  _model     = data.get('model', None)
  _values    = data.get('values', None)
  _filters   = data.get('filters', None)

  _data = []

  _model = getModel(_app, _model)

  if _model:
    try:

      _data = _model.all()

      if _filters:
        _data = _data.filter(**_filters)

      _data = await _data.values(*_values)

    except Exception as ex:
      print(f"[getModelData] {ex}")

  params = {
    "code" : code,
    "msg"  : msg,
    "data" : _data
  }

  return params

async def ViewUser(request,pk=None):
  from globaltechia.base.models import User

  code  = 200
  msg   = "Operación realizada con éxito"
  _form = None
  obj   = None

  if pk:
    obj = await User.filter(id=pk).last()

  if request.method == 'GET':
    _form = await User.schema(obj=obj)
  else:
    data = await request.json()

    del data['password']
    del data['confirm_password']

    try:
      if not obj:
        obj = await User.create(**data)
      else:
        await User.filter(id=pk).update(**data)
    except Exception as ex:
      print(ex)

  params = {
    "code"         : code,
    "msg"          : msg,
    "form"         : _form,
    "obj"          : obj,
    "verbose_name" : User.Meta.verbose_name if User.Meta.verbose_name else 'User',
  }

  return params


async def removeItems(request):
  import json

  data = await request.json()

  app   = data.get('app',None)
  view  = data.get('view',None)
  data  = data.get('data',[])

  if app and view and data:

    data = json.loads(data)
    _model = getModel(app,view)
    try:
      await _model.filter(id__in=data).delete()
    except Exception as ex:
      pass

  params = {
    "code" : 200,
    "msg"  : "Operación realizada con éxito"
  }

  return params

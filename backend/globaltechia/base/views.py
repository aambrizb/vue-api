from globaltechia.base.models import Navbar
from globaltechia.utils import getModel
import json
import importlib
import os
async def navbar(request):

  data = await Navbar.filter(parent_id=None).values()

  for item in data:
    item['children'] = await Navbar.filter(
      parent_id=item['id']
    ).values()

  return data

async def login(request):
  from base.models import User

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
      await _model.filter(id=_id).delete()
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

async def ApiToken_view(request,pk=None):
  from base.models import ApiToken
  import uuid

  _form = None
  obj   = None

  if pk:
    obj = await ApiToken.filter(id=pk).last()

  if request.method == 'GET':
    _form = await ApiToken.schema(obj=obj)
  elif request.method == 'POST':
    data = await request.json()
    data['token'] = str(uuid.uuid4())
    try:
      if not obj:
        obj = await ApiToken.create(**data)
      else:
        await ApiToken.filter(id=pk).update(**data)
    except Exception as ex:
      print(ex)

  return {
    "form" : _form,
    "obj"  : obj
  }

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

async def User_view(request,pk=None):
  from base.models import User

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
    "code" : code,
    "msg"  : msg,
    "form" : _form,
    "obj"  : obj
  }

  return params
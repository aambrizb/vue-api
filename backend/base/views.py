from base.models import Navbar
import json

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
      obj = await ApiToken.create(**data)
    except Exception as ex:
      print(ex)

  return {
    "form" : _form,
    "obj"  : obj
  }

from base.models import Navbar
import json

async def navbar(request,id=None):

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

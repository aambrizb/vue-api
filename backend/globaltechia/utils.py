from tortoise.models import Model
from tortoise import fields
from fastapi import HTTPException
from tortoise.queryset import QuerySet
from argon2 import PasswordHasher, Type
from functools import wraps
import math
import importlib
import os

PACKAGE_NAME = 'globaltechia'

def login_required(func):
  @wraps(func)
  async def wrapper(*args, **kwargs):
    from globaltechia.base.models import User

    request: Request = kwargs.get("request") or args[0]
    token = request.headers.get("Authorization")
    _url = request.get('path')

    if 'base/login' in _url or 'base/logout' in _url:
      return await func(*args, **kwargs)

    if token:
      token = token.split("Bearer ")
      if len(token) == 2:
        _user = await User.filter(token=token[1],active=True).last()

        if not _user:
          raise HTTPException(status_code=401, detail="Unauthorized")

        return await func(*args, **kwargs)

    else:
      raise HTTPException(status_code=401, detail="Unauthorized")

  return wrapper

def getToken(request):

  _auth  = request.headers.get("authorization","")
  _auth  = _auth.split("Bearer ")
  _token = ""

  if len(_auth) == 2:
    _token = _auth[1]

  return _token

def getModel(app,model):

  if app == 'base':
    app = f'{PACKAGE_NAME}.{app}'

  _model  = None
  _module = importlib.import_module(f'{app}.models')

  if _module and hasattr(_module, model):
    _model = getattr(_module, model)

  return _model

def getView(app,method,prefix=""):

  _view       = None
  _globaltech = ''

  if app == 'base':
    app = f'{PACKAGE_NAME}.{app}'

  _prefix = f'{prefix}{method}'

  _module = importlib.import_module(f'{app}.views')

  if _module and hasattr(_module, _prefix):
    _view = getattr(_module, _prefix)

  return _view
class Pagination:
  data          = None
  list_per_page = 100
  total_pages   = 0
  current_page  = 0

  def __init__(self,data,list_per_page=100,page=1):

    self.data          = data
    self.list_per_page = list_per_page
    self.current_page  = page

    if len(data) > 0:
      self.total_pages   = int(math.ceil(len(data) / self.list_per_page))

  def getProps(self):
    return {
      'list_per_page' : self.list_per_page,
      'current_page'  : self.current_page,
      'total_pages'   : self.total_pages
    }

  def getData(self):

    if not self.current_page:
      self.current_page = 1

    if not self.list_per_page:
      self.list_per_page = 100

    _start = (int(self.current_page)-1)*int(self.list_per_page)
    _end   = _start+int(self.list_per_page)

    _final_data = self.data[_start:_end]

    return _final_data

class FrameField:
  name         = None
  label        = None
  help_text    = None
  #required     = False
  label_class  = ''
  input_class  = ''
  type         = None
  choices      = []
  disabled     = False
  error        = None
  value        = None
  klass        = ''
  show         = True

  def __init__(
    self,
    *,
    type        = None,
    name        = None,
    label       = None,
    help_text   = None,
    #required    = False,
    label_class = 'col-lg-2 col-md-2 col-sm-2 col-xs-12',
    input_class = 'col-lg-2 col-md-2 col-sm-2 col-xs-12',
    choices     = [],
    disabled    = False,
    error       = None,
    value       = None,
    klass       = 'form-control',
    show        = True,
    default     = False,
    **kwargs
  ):

    if type:
      self.type          = type

    if self.type == 'checkbox':
      klass = ''

    self.name          = name
    self.label         = label

    self.help_text     = help_text
    #self.required      = required
    self.label_class   = label_class
    self.input_class   = input_class
    self.choices       = choices
    self.disabled      = disabled
    self.error         = error
    self.value         = value
    self.label_class   = label_class
    self.input_class   = input_class
    self.klass         = klass
    self.show          = show
    self.default       = default

    super().__init__(**kwargs)

  def schema(self,name,value=None,choices=[]):
    self.name = name

    self.value = value

    if not self.label:
      self.label = self.name.capitalize()

    self.choices = choices

    _tmp = {
      "type"         : self.type,
      "name"         : self.name,
      "label"        : self.label,
      "help_text"    : self.help_text,
      #"required"     : self.required,
      "choices"      : self.choices,
      "disabled"     : self.disabled,
      "error"        : self.error,
      "value"        : self.value if self.value else self.default,
      "klass"        : self.klass,
      "label_class"  : self.label_class,
      "input_class"  : self.input_class,
      "default"      : self.default,
      "show"         : self.show,
      "selected"     : False
    }

    return _tmp

class CharField(FrameField,fields.CharField):
  type = 'text'

class IntField(FrameField,fields.IntField):
  type = 'text'

class DateField(FrameField,fields.DateField):
  type  = 'date'

class DatetimeField(FrameField,fields.DatetimeField):
  type  = 'datetime-local'

class BooleanField(FrameField,fields.BooleanField):
  type  = 'checkbox'
  klass = ''

class FloatField(FrameField,fields.FloatField):
  type  = 'text'

class ForeignKeyFieldInstance(fields.relational.ForeignKeyFieldInstance,FrameField):
  def __init__(self, model_name, *args, **kwargs):

    frame_kwargs = {
      "type":"select",
      "klass":"form-select"
    }

    for key in [
      "type", "name", "label", "help_text",
      "label_class", "input_class", "choices", "disabled",
      "error", "value", "klass", "show"
    ]:
      if key in kwargs:
        frame_kwargs[key] = kwargs.pop(key)

    super().__init__(model_name, *args, **kwargs)

    FrameField.__init__(self, **frame_kwargs)

  async def get_choices(self):
    if not hasattr(self, "related_model") or not self.related_model:
      raise RuntimeError("Model not initialized yet. Did you call Tortoise.init()?")

    data = await self.related_model.all()
    _init = [{"label":"--","value":""}]
    return _init+[{"label":str(obj), "value":obj.pk} for obj in data]

def ForeignKeyField(model_name, **kwargs):
  return ForeignKeyFieldInstance(model_name, **kwargs)

class FrameModel(Model):

  id = IntField(pk=True,show=False)

  class Meta:
    verbose_name = None
  @classmethod
  async def schema(self,obj=None):
    tmp = {}

    for x in self._meta.fields_map:
      if isinstance(self._meta.fields_map[x],FrameField) and not isinstance(self._meta.fields_map[x],ForeignKeyFieldInstance):
        _schema = self._meta.fields_map[x].schema(x,getattr(obj,x) if obj else None)
        if _schema['show']:
          tmp[x] = _schema
      if isinstance(self._meta.fields_map[x],ForeignKeyFieldInstance):
        _tmp = await self._meta.fields_map[x].get_choices()
        _field = f"{x}_id"
        _schema = self._meta.fields_map[x].schema(_field, getattr(obj, f"{x}_id") if obj else None,_tmp)
        if _schema['show']:
          tmp[_field] = _schema

    return tmp

def SecretHash():
  ph = PasswordHasher(
      time_cost   = 2,
      memory_cost = 102400,
      parallelism = 8,
      hash_len    = 32,
      salt_len    = 16,
      type        = Type.ID
  )

  return ph

def GeneratePassword(password):
  ph = SecretHash()
  return ph.hash(password)

def VerifyPassword(hash,password):
  ph = SecretHash()

  try:
    ph.verify(hash, password)
    return True
  except Exception as ex:
    pass

  return False

async def getUserPermissions(token):
  from globaltechia.base.models import (
    User,
    UserGroup,
    UserPermission,
    GroupPermission,
    Permission
  )

  ar_permissions   = []
  _userpermissions = []

  obj            = await User.filter(token=token).last()

  if obj:
    if not obj.superuser:
      _groups          = await UserGroup.filter(user_id=obj.id).values_list('group_id',flat=True)
      _userpermissions = await UserPermission.filter(user_id=obj.id).values_list('permission__name',flat=True)
      ar_permissions   = await GroupPermission.filter(group_id__in=_groups).values_list('permission__name',flat=True)
    else:
      ar_permissions = await Permission.all().values_list('name',flat=True)

    ar_permissions = ar_permissions+_userpermissions

  return ar_permissions

async def getUserGroups(token):
  from globaltechia.base.models import UserGroup

  ar_groups = await UserGroup.filter(
    user__token=token
  ).values_list('group__name',flat=True)

  return ar_groups

async def hasPermission(token,permission):

  ar_permissions = await getUserPermissions(token)
  if permission in ar_permissions:
    return True

  return False

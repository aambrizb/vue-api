from tortoise.models import Model
from tortoise import fields
import math

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

    _start = (int(self.current_page)-1)*int(self.list_per_page)
    _end   = _start+int(self.list_per_page)

    _final_data = self.data[_start:_end]

    return _final_data

class FrameField:
  name         = None
  label        = None
  help_text    = None
  required     = False
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
    required    = False,
    label_class = 'col-lg-2 col-md-2 col-sm-2 col-xs-12',
    input_class = 'col-lg-2 col-md-2 col-sm-2 col-xs-12',
    choices     = [],
    disabled    = False,
    error       = None,
    value       = None,
    klass       = 'form-control',
    show        = True,
    **kwargs
  ):

    if type:
      self.type          = type

    if self.type == 'checkbox':
      klass = ''

    self.name          = name
    self.label         = label

    self.help_text     = help_text
    self.required      = required
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

    super().__init__(**kwargs)

  def schema(self,name,value=None):

    self.name = name

    if value:
      self.value = value;

    if not self.label:
      self.label = self.name.capitalize()

    return {
      "type"         : self.type,
      "name"         : self.name,
      "label"        : self.label,
      "help_text"    : self.help_text,
      "required"     : self.required,
      "choices"      : self.choices,
      "disabled"     : self.disabled,
      "error"        : self.error,
      "value"        : self.value,
      "klass"        : self.klass,
      "label_class"  : self.label_class,
      "input_class"  : self.input_class,
      "show"         : self.show,
      "selected"     : False
    }

class CharField(FrameField,fields.CharField):
  type = 'text'

class IntField(FrameField,fields.IntField):
  type = 'text'

class DatetimeField(FrameField,fields.DatetimeField):
  type  = 'datetime-local'

class BooleanField(FrameField,fields.BooleanField):
  type  = 'checkbox'
  klass = ''

class FrameModel(Model):

  id = IntField(pk=True,show=False)

  @classmethod
  def schema(self,obj=None):
    tmp = {}

    for x in self._meta.fields_map:
      if isinstance(self._meta.fields_map[x],FrameField):
        _schema = self._meta.fields_map[x].schema(x,getattr(obj,x) if obj else None)
        if _schema['show']:
          tmp[x] = _schema

    return tmp

class Navbar(FrameModel):
  name       = CharField(max_length=120)
  to         = CharField(max_length=120,null=True)
  app        = CharField(max_length=60,null=True)
  view       = CharField(max_length=60,null=True)
  icon_class = CharField(max_length=160,null=True)
  order      = IntField(default=0)
  parent:      fields.ForeignKeyRelation["Navbar"] = fields.ForeignKeyField(
    'models.Navbar',
    null=True,
    on_delete=fields.RESTRICT,

  )
  active     = fields.BooleanField(default=True)

  def __str__(self):
    return self.name

class Permission(FrameModel):
  name   = CharField(max_length=20)
  active = BooleanField(default=True)

class FrameAdmin:
  list_display = []
  search_field = []

class Group(FrameModel):
  name   = CharField(label='Nombre',help_text='Aqui puede ingresar el nombre',max_length=120)
  active = BooleanField(label='Activo',help_text='indica que se encuentra activo o no',default=True)

  #class Admin(FrameAdmin):
  #  list_display = ['name','active']
  #  search_field = ['name']


  def __str__(self):
    return self.name

class GroupPermission(Model):

  group: fields.ForeignKeyRelation[Group] = fields.ForeignKeyField(
    'models.Group',
    on_delete=fields.RESTRICT
  )
  permission: fields.ForeignKeyRelation[Permission] = fields.ForeignKeyField(
    'models.Permission',
    on_delete=fields.RESTRICT
  )

class User(FrameModel):
  first_name  = CharField(max_length=45,label="Nombre",help_text="Ingrese nombre completo. ej. Alejandro")
  last_name   = CharField(max_length=45,label="Apellido Paterno",help_text="Apellido Paterno ej. Ambríz")
  middle_name = CharField(max_length=45,label="Apellido Materno",help_text="Apellido Materno ej. Bedolla")
  email       = CharField(max_length=120)
  password    = CharField(max_length=220)
  token       = CharField(max_length=220,null=True,show=False)
  last_login  = DatetimeField(show=False,null=True)
  superuser = BooleanField(default=False,label='Super-Usuario')
  active      = BooleanField(default=True,label="Activo")

  class Admin:
    list_display  = ['id','first_name','last_name','middle_name','email']
    list_per_page = 2
    #search_field = ['first_name']

  def __str__(self):
    return self.email

class UserGroup(Model):
  user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
    'models.User',
    on_delete=fields.RESTRICT
  )
  group: fields.ForeignKeyRelation[Group] = fields.ForeignKeyField(
    'models.Group',
    on_delete=fields.RESTRICT
  )

class UserPermission(Model):
  user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
    'models.User',
    on_delete=fields.RESTRICT
  )
  permission: fields.ForeignKeyRelation[Permission] = fields.ForeignKeyField(
    'models.Permission',
    on_delete=fields.RESTRICT
  )

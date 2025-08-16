from tortoise.models import Model
from tortoise import fields

class FrameModel(Model):
  @classmethod
  def schema(self):

    tmp = []

    for x in self._meta.fields_map:
      if isinstance(self._meta.fields_map[x],FrameField):
        tmp.append(self._meta.fields_map[x].schema(x))

    return tmp

class FrameField:
  verbose_name = None
  help_text    = None
  required     = False
  label_class  = ''
  input_class  = ''
  type         = None
  choices      = []
  disabled     = False

  def __init__(self,*,verbose_name=None,help_text=None,required=False,label_class='',input_class='',type=None,choices=[],disabled=False,**kwargs):

    self.verbose_name  = verbose_name
    self.help_text     = help_text
    self.required      = required
    self.label_class   = label_class
    self.input_class   = input_class
    self.type          = type
    self.choices       = choices
    self.disabled      = disabled

    super().__init__(**kwargs)

  def schema(self,name):
    return {
      "name"         : name,
      "verbose_name" : self.verbose_name,
      "help_text"    : self.help_text,
      "required"     : self.required,
      "label_class"  : self.label_class,
      "input_class"  : self.input_class,
      "type"         : self.type,
      "choices"      : self.choices,
      "disabled"     : self.disabled
    }
class CharField(FrameField,fields.CharField):
  type = 'text'

class IntField(FrameField,fields.IntField):
  type = 'text'

class BooleanField(FrameField,fields.BooleanField):
  type = 'checkbox'

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

class Group(FrameModel):
  name   = CharField(verbose_name='Nombre',help_text='Aqui puede ingresar el nombre',max_length=120)
  active = BooleanField(verbose_name='Activo',help_text='indica que se encuentra activo o no',default=True)

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

class User(Model):
  first_name  = fields.CharField(max_length=45)
  last_name   = fields.CharField(max_length=45)
  middle_name = fields.CharField(max_length=45)
  email       = fields.CharField(max_length=120)
  password    = fields.CharField(max_length=220)
  token       = fields.CharField(max_length=220)
  last_login  = fields.DatetimeField()
  active      = fields.BooleanField(default=True)

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

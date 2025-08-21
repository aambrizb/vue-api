from tortoise.models import Model
from tortoise import fields
import utils
class Navbar(utils.FrameModel):
  name       = utils.CharField(max_length=120)
  to         = utils.CharField(max_length=120,null=True)
  app        = utils.CharField(max_length=60,null=True)
  view       = utils.CharField(max_length=60,null=True)
  icon_class = utils.CharField(max_length=160,null=True)
  order      = utils.IntField(default=0)
  parent:      fields.ForeignKeyRelation["Navbar"] = utils.ForeignKeyField(
    'models.Navbar',
    null=True,
    on_delete=fields.RESTRICT,
    label="Padre"
  )
  active     = fields.BooleanField(default=True)

  def __str__(self):
    return self.name

class Permission(utils.FrameModel):
  name   = utils.CharField(max_length=20)
  active = utils.BooleanField(default=True)

class FrameAdmin:
  list_display = []
  search_field = []

class Group(utils.FrameModel):
  name   = utils.CharField(label='Nombre',help_text='Aqui puede ingresar el nombre',max_length=120)
  active = utils.BooleanField(label='Activo',help_text='indica que se encuentra activo o no',default=True)

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

class User(utils.FrameModel):
  first_name  = utils.CharField(max_length=45,label="Nombre",help_text="Ingrese nombre completo. ej. Alejandro")
  last_name   = utils.CharField(max_length=45,label="Apellido Paterno",help_text="Apellido Paterno ej. Ambríz")
  middle_name = utils.CharField(max_length=45,label="Apellido Materno",help_text="Apellido Materno ej. Bedolla")
  email       = utils.CharField(max_length=120)
  password    = utils.CharField(max_length=220)
  token       = utils.CharField(max_length=220,null=True,show=False)
  last_login  = utils.DatetimeField(show=False,null=True)
  superuser   = utils.BooleanField(default=False,label='Super-Usuario')
  active      = utils.BooleanField(default=True,label="Activo")

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

class ApiToken(utils.FrameModel):
  name   = utils.CharField(max_length=120,label="Nombre")
  token  = utils.CharField(max_length=255,show=False)
  active = utils.BooleanField(default=True, label="Activo")

  def __str__(self):
    return self.name

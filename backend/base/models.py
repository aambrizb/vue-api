from tortoise.models import Model
from tortoise import fields

class Navbar(Model):
  name       = fields.CharField(max_length=120)
  to         = fields.CharField(max_length=120)
  app        = fields.CharField(max_length=60)
  view       = fields.CharField(max_length=60)
  icon_class = fields.CharField(max_length=160)
  order      = fields.IntField(default=0)
  parent:      fields.ForeignKeyRelation["Navbar"] = fields.ForeignKeyField(
    'models.Navbar',
    on_delete=fields.RESTRICT
  )
  active     = fields.BooleanField(default=True)

  def __str__(self):
    return name

class Permission(Model):
  name   = fields.CharField(max_length=20)
  active = fields.BooleanField(default=True)

class Group(Model):
  name   = fields.CharField(max_length=120)
  active = fields.BooleanField(default=True)

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
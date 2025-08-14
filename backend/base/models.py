from tortoise.models import Model
from tortoise import fields

class Group(Model):
  name   = fields.CharField(max_length=120)
  active = fields.BooleanField(default=True)

class User(Model):
  first_name  = fields.CharField(max_length=45)
  last_name   = fields.CharField(max_length=45)
  middle_name = fields.CharField(max_length=45)
  email       = fields.CharField(max_length=120)
  groups      = fields.ManyToManyField('models.Group', related_name='users')
  active      = fields.BooleanField(default=True)



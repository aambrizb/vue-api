import asyncio
from tortoise import Tortoise, run_async
from main import DATABASE_CONFIG
from pathlib import Path
from globaltechia import utils
import os
import inspect
import json

async def init():
  await Tortoise.init(config=DATABASE_CONFIG)
  await Tortoise.generate_schemas()

def start_shell():
  try:
    from IPython import embed
    from traitlets.config import Config

    cfg = Config()
    cfg.InteractiveShellEmbed.autoawait = True
    cfg.InteractiveShellEmbed.loop_runner = "asyncio"

    embed(config=cfg, banner1="TortoiseORM async shell (IPython)")
  except ImportError:
    import code
    code.interact(local=globals())

async def createsuperuser():
  from globaltechia.base.models import User
  from globaltechia.utils import GeneratePassword

  _name   = input("Type your Firstname: ")
  _last   = input("Type your Lastname: ")
  _email  = input("Type your email: ")
  _passwd = input("Type your password: ")

  if _name and _email and _passwd:

    obj = await User.filter(email=_email).first()

    if not obj:
      await User.create(
        first_name = _name,
        last_name  = _last,
        email      = _email,
        superuser  = True,
        active     = True,
        password   = GeneratePassword(_passwd)
      )

      print("[CREATE] Superuser.")
    else:
      print("[ERROR] User already created.")
async def resetpassword():
  from globaltechia.base.models import User
  from globaltechia.utils import GeneratePassword

  _email  = input("Type your email: ")
  _passwd = input("Type your password: ")

  if _email and _passwd:

    obj = await User.filter(email=_email).first()

    if not obj:
      print("[ERROR] User does not exist")
    else:
      obj.password = GeneratePassword(_passwd)
      await obj.save()
      print("[OK] User password changed.")

async def set_permissions():
  from globaltechia.base.models import Navbar, Permission

  data = await Navbar.all().values()
  for item in data:
    if item['app'] and item['view']:

      _permissions = ['view','save','delete']
      for x in _permissions:
        _permission = f'{item["app"]}.{item["view"]}.{x}'
        obj = await Permission.filter(name=_permission).last()
        if not obj:
          await Permission.create(name=_permission,active=True)
          print(f"[OK] {_permission}")

async def dump_data(app,model):

  _model = utils.getModel(app, model)

  if _model:
    data = await _model.all().values()
    print(json.dumps(data,indent=2))
async def load_data():
  from globaltechia.base.models import User

  dir_globaltechia = inspect.getfile(User)

  DATA_BASE_PATHS = [
    os.getcwd(),
    dir_globaltechia
  ]

  for y in DATA_BASE_PATHS:
    BASE_DIR = Path(y).resolve()
    for path in BASE_DIR.rglob("*.json"):
      if "data" in path.parent.name:
        try:
          _app,_model,_ext = path.name.split(".")
          _mod = utils.getModel(_app,_model)
          if _mod:
            with open(path, "r", encoding="utf-8") as f:
              read_data = json.load(f)
              for x in read_data:

                _tmp_id = x.get('id',None)

                _obj = await _mod.filter(id=_tmp_id).last()
                if _obj:
                  del x['id']
                  await _mod.filter(id=_tmp_id).update(**x)
                  print(f"[UPDATED] {_app}.{_model} {_tmp_id}")
                else:
                  _obj = await _mod.create(**x)
                  print(f"[CREATED] {_app}.{_model} {_obj.id}")
        except Exception as ex:
          print(ex)



if __name__ == "__main__":
  import sys

  loop = asyncio.get_event_loop()
  if not loop.is_running():
    loop.run_until_complete(init())
  else:
    loop.create_task(init())

  if len(sys.argv) >= 2:
    if sys.argv[1] == 'shell':
      start_shell()
    elif sys.argv[1] == 'create_superuser':
      run_async(createsuperuser())
    elif sys.argv[1] == 'reset_password':
      run_async(resetpassword())
    elif sys.argv[1] == 'set_permissions':
      run_async(set_permissions())
    elif sys.argv[1] == 'dump_data':
      if len(sys.argv) == 4:
        _app  = sys.argv[2]
        _model = sys.argv[3]
        run_async(dump_data(_app,_model))
      else:
        print("[Syntax] dump_data <app> <model>")
    elif sys.argv[1] == 'load_data':
      run_async(load_data())
  else:
    print("[Commands]")
    print("\t shell            | Access Shell")
    print("\t create_superuser | Create Superuser")
    print("\t reset_password   | Reset Password")
    print("\t set_permissions  | Set Default Permissions (Navbar)")
    print("\t dump_data        | Dump data ")
    print("\t load_data        | Load data")

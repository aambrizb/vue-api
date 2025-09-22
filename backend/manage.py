import asyncio
from tortoise import Tortoise, run_async
from main import DATABASE_CONFIG

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
      _permission = f'{item["app"]}.{item["view"]}.view'
      obj = await Permission.filter(name=_permission).last()
      if not obj:
        await Permission.create(name=_permission,active=True)
        print(f"[OK] {_permission}")


if __name__ == "__main__":
  import sys

  loop = asyncio.get_event_loop()
  if not loop.is_running():
    loop.run_until_complete(init())
  else:
    loop.create_task(init())

  if len(sys.argv) == 2:
    if sys.argv[1] == 'shell':
      start_shell()
    elif sys.argv[1] == 'create_superuser':
      run_async(createsuperuser())
    elif sys.argv[1] == 'reset_password':
      run_async(resetpassword())
    elif sys.argv[1] == 'set_permissions':
      run_async(set_permissions())
  else:
    print("[Commands]")
    print("\t shell            | Access Shell")
    print("\t create_superuser | Create Superuser")
    print("\t reset_password   | Reset Password")
    print("\t set_permissions  | Set Default Permissions (Navbar)")

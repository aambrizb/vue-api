import os
import glob
import shutil
import subprocess
import sys
def main():

  original_path = os.getcwd()

  print("[RESTORE] BackEnd Project.")

  # Reset Backend Folder
  if os.path.isdir('builds/be-globaltechia/globaltechia'):
    shutil.rmtree('builds/be-globaltechia/globaltechia')

  if os.path.isdir('builds/be-globaltechia/dist'):
    shutil.rmtree('builds/be-globaltechia/dist')

  # Copy Last Background Project
  print("[COPY] BackEnd Project")
  shutil.copytree('backend/globaltechia', 'builds/be-globaltechia/globaltechia',dirs_exist_ok=True)

  print("[BUILD] Create BackEndBuild")

  os.chdir("builds/be-globaltechia")
  subprocess.check_call([sys.executable, "-m", "build"])

  os.chdir(original_path)

  print("[RESTORE] FrontEnd Project.")

  # Reset FrontEnd Folder
  if os.path.isdir('builds/globaltechia/src/components'):
    shutil.rmtree('builds/globaltechia/src/components')

  if os.path.isdir('builds/globaltechia/src/modals'):
    shutil.rmtree('builds/globaltechia/src/modals')

  if os.path.isdir('builds/globaltechia/src/theme'):
    shutil.rmtree('builds/globaltechia/src/theme')

  if os.path.isdir('builds/globaltechia/src/views'):
    shutil.rmtree('builds/globaltechia/src/views')

  # Copy Last FrontEnd Project
  print("[COPY] FrontEnd Project")

  shutil.copytree('src/globaltechia', 'builds/globaltechia/src',dirs_exist_ok=True)

  print("[BUILD] Create FrontEnd Build")

  os.chdir("builds/globaltechia")

  subprocess.check_call(["npm", "install"])
  subprocess.check_call(["npm", "run","prebuild"])
  subprocess.check_call(["npm", "run","build"])
  subprocess.check_call(["npm", "pack"])

main()
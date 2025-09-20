import os
import glob
import shutil
import subprocess
import sys
def main():

  print("[RESTORE] BackEnd Project.")

  # Reset Backend Folder
  shutil.rmtree('builds/be-globaltechia/globaltechia')
  shutil.rmtree('builds/be-globaltechia/dist')

  # Copy Last Project
  print("[COPY] BackEnd Project")
  shutil.copytree('backend/globaltechia', 'builds/be-globaltechia/globaltechia',dirs_exist_ok=True)

  print("[BUILD] Create Build")

  os.chdir("builds/be-globaltechia")
  subprocess.check_call([sys.executable, "-m", "build"])


main()
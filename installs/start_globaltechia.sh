#!/bin/bash
set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <project_name>"
  exit 1
fi

APP_NAME="$1"

if [ -d "$APP_NAME" ]; then
  echo "Directory '$APP_NAME' already exists, skipping GlobalTechIA  setup."
  exit
fi

mkdir $APP_NAME
cd $APP_NAME

# Prepare Installs
mkdir installs
cd installs
curl -L -o globaltechia-1.0.0.tgz https://github.com/aambrizb/vue-api/raw/refs/heads/main/installs/globaltechia-1.0.0.tgz
curl -L -o be_globaltechia-0.1.0.tar.gz https://github.com/aambrizb/vue-api/raw/refs/heads/main/installs/be_globaltechia-0.1.0.tar.gz
cd ..

# Prepare Backend
mkdir backend
cd backend
curl -L -o main.py https://github.com/aambrizb/vue-api/raw/refs/heads/main/backend/main.py
curl -L -o manage.py https://github.com/aambrizb/vue-api/raw/refs/heads/main/backend/manage.py
echo '../installs/be_globaltechia-0.1.0.tar.gz' > requirements.txt
python3 -m venv vython
source vython/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
cd ..

# Prepare FrontEnd
npm create vue@latest frontend -- --router
cd frontend
npm install
npm install bootstrap --save
npm install @fortawesome/fontawesome-free --save
npm install ../installs/globaltechia-1.0.0.tgz --save

# Change Vue Files to GlobalTechia Files
rm -rf src/main.js
curl -L -o src/main.js https://github.com/aambrizb/vue-api/raw/refs/heads/main/installs/example.main.js

rm -rf src/router/index.js
curl -L -o src/router/index.js https://github.com/aambrizb/vue-api/raw/refs/heads/main/installs/example.default_router.js
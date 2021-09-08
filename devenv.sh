#!/bin/bash

# TODO: (lgruelas) Add cli usage, init, check, down.

DB_ENV=db/.env
#BE_ENV=backend/backend/settings/dev.py
#FE_ENV=frontend/.env

if test -f "$DB_ENV"; then
    echo "Please clean your environment, cannot init."
    exit 1
else
    cp db/.env.example db/.env
    cp frontend/.env.docker.example frontend/.env
    cp backend/backend/settings/example.py backend/backend/settings/dev.py
    SECRET_KEY=$(base64 /dev/urandom | head -c50)
    sed -i "8iSECRET_KEY = '$SECRET_KEY'" backend/backend/settings/dev.py
    touch .env.codecov
fi

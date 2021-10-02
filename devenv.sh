#!/bin/bash

COMMAND="$1"

DB_ENV=db/.env
BE_ENV=backend/backend/settings/dev.py
FE_ENV=frontend/.env


checkEnv() {
    if test -f "$DB_ENV" && test -f "$BE_ENV" && test -f "$FE_ENV"; then
        return
    fi
    false
}


if [ $COMMAND = "init" ]; then
    if checkEnv; then
        echo "Please clean your environment with ./devenv.sh down"
        exit 1
    else
        cp db/.env.example db/.env
        cp frontend/.env.docker.example frontend/.env
        cp backend/backend/settings/example.py backend/backend/settings/dev.py
        SECRET_KEY=$(base64 /dev/urandom | head -c50)
        sed -i "8iSECRET_KEY = '$SECRET_KEY'" backend/backend/settings/dev.py
        touch .env.codecov
        echo "Devenv initialized succesfully."
    fi
elif [[ $COMMAND == "check" ]]; then
    if checkEnv; then
        echo "Files are created, check manually the django settings if something is wrong."
    else
        echo "Files are not created, please run ./devenv.sh init"
    fi
elif [ $COMMAND = "down" ]; then
    rm db/.env
    rm frontend/.env
    rm backend/backend/settings/dev.py
    rm .env.codecov
else
    echo "Unknown command, please use init, down or check as parameter."
    exit 1
fi

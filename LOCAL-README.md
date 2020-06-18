## Prerequisites

You must have a functional version of **Node**, **npm** and **Python**, the frontend is working with **React** and the backend is in **Django**. The database is in **Postrgesql** so you also should have one. Still you might face issues with **psycopg2**

## Instalation

### Env files

-   `frontend/.env.local.example` - please rename it to `.env`
-   `backend/backend/settings/example.py` - please rename it to `local.py` and fill as required.

**Note:** It's really important to make `source .env.local` in the root directory.

### Database

First create the database and user for the app.
```bash
psql postgres
```
```postgres
CREATE DATABASE finance;
CREATE USER django_user PASSWORD 'localpassword';
GRANT ALL PRIVILEGES ON DATABASE finance TO django_user;
```

### Backend

Install python and virtualenv.

```bash
sudo dnf -y install python3
sudo dnf -y install python3-pip
pip3 install --user virtualenv
```

Then create the virtual enviroment.

```bash
virtualenv -p python3 venv
```

if It fails try with
```bash
python -m virtualenv -p python3 venv
```
To start the virtual enviroment use:

```bash
source venv/bin/activate
```
then install dependencies
```bash
cd backend
pip install -r requirements.txt
```

to exit the virtual environment just run
```bash
deactivate
```

### Frontend

Install the frontend dependencies with
```bash
cd frontend
npm install
```

## Run the App

to run the frontend and the backend just use:
```bash
honcho -e .env.local start
```

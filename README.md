[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d2f8cf8fe58645f8a94bf4d85e8ba056)](https://app.codacy.com/manual/lgruelas/finance?utm_source=github.com&utm_medium=referral&utm_content=lgruelas/finance&utm_campaign=Badge_Grade_Dashboard)
[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
[![license](https://img.shields.io/badge/licence-GPL--3-blue.svg)](https://github.com/lgruelas/finance/blob/master/LICENSE)
[![Build Status](https://api.travis-ci.com/lgruelas/finance.svg?branch=master)](https://travis-ci.com/lgruelas/finance)
# Personal Finance Administrator

![Python master race](assets/python.png?raw=true "python")

## Getting started
This project has been made only for study porpouses, it allows you to administrate budgets for each category of your expenses, manage your accounts and so on, later on I might upload a demo video, for now it is under construction.

### Prerequisites

#### Local dev without docker

You must have a functional version of **Node**, **npm** and **Python**, the frontend is working with **React** and the backend is in **Django**. The database is in **Postrgesql** so you also should have one.

#### Local dev with docker

You just need to have **docker** and been logged.

### Installation

First create the database and user for the app.
```bash
psql postgres
```
```postgres
CREATE DATABASE finance;
CREATE USER django_user PASSWORD 'localpassword';
GRANT ALL PRIVILEGES ON DATABASE finance TO django_user;
```

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

if fails try with
```bash
python -m virtualenv -p python3 venv
```
To start the virtual enviroment use:

```bash
source venv/bin/activate
```
then install dependencies
```bash
pip install django
pip install honcho
```

to exit the virtual environment just run
```bash
deactivate
```

Install the frontend dependencies with
```bash
cd frontend
npm install
```
## Dev run
to run the frontend and the backend just use:
```bash
honcho start
```

## Built With

*   [Python](https://www.python.org/downloads/)
*   [Django](https://www.djangoproject.com/download/)
*   [Typescript](https://www.typescriptlang.org/index.html#download-links)
*   [React](https://reactjs.org/)

## Authors

*   **Germán Ruelas** - [GitHub](https://github.com/lgruelas)

## License

This project is licensed under the GPL 3 License - see the [LICENSE.md](LICENSE.md) file for details

## Project Status

I'm starting it.

## Versioning

I'll be unisg semver for versioning.

### Current version

The first release will be soon, I just need to add unittests and set up CI and codecov.
You can always check the [CHANGELOG](https://github.com/lgruelas/finance/blob/master/CHANGELOG.md).

## Contributing

All contribution is thanked and encouraged, just follow [these lines](https://github.com/lgruelas/finance/blob/master/CHANGELOG.md).


[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
[![license](https://img.shields.io/badge/licence-GPL--3-blue.svg)](https://github.com/lgruelas/finance/blob/master/LICENSE)
[![Build Status](https://api.travis-ci.com/lgruelas/finance.svg?branch=master)](https://travis-ci.com/lgruelas/finance)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/0409d1607cb04aef95cfb96f4af42887)](https://www.codacy.com/manual/lgruelas/finance?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lgruelas/finance&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/lgruelas/finance/branch/master/graph/badge.svg)](https://codecov.io/gh/lgruelas/finance)

# Personal Finance Administrator

![Python master race](assets/python.png?raw=true "python")

## Getting started

This project has been made only for study porpouses, it allows you to administrate budgets for each category of your expenses, manage your accounts and so on, later on I might upload a demo video, for now it is under construction.

There are two ways to set it up for use and for development, using a regular local env (now deprecated, but you can still see the instructions [here](htts://github.com/lgruelas/finance/blob/master/LOCAL-README.md)) and a docker environment.

### Prerequisites

You just need to have **docker** and been logged.

### Installation

For all the configurations you should keep an eye in 3 files:
-   `db/.env.example` - please rename it to `.env`
-   `frontend/.env.docker.example` - please rename it to `.env`
-   `backend/backend/settings/example.py` - please rename it to `dev.py` and fill as required.
-   Create an empty file at root called `.env.codecov`, this is needed in the CI env.

Then you just need to build the images, containers but this is done with the first run.

### Run the App

Just use
```bash
docker-compose up -d
```

### Stop the app

```bash
docker-compose down
```

**Note:** due to the volumes, the database info is persistent, to remove it permanently use:

```bash
dacker-compose down -v
```

And then erase the images and containers with `docker images rm <image-id>` and `docker rm <container-id>`

## Built With

-   [Python](https://www.python.org/downloads/)
-   [Django](https://www.djangoproject.com/download/)
-   [Typescript](https://www.typescriptlang.org/index.html#download-links)
-   [React](https://reactjs.org/)

## Authors

-   **Germán Ruelas** - [GitHub](https://github.com/lgruelas)
If you need help with running the system feel free to send me an email.

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

All contribution is thanked and encouraged, just follow [these lines](https://github.com/lgruelas/finance/blob/master/CONTRIBUTING.md).


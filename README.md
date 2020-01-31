[![license](https://img.shields.io/badge/licence-GPL--3-blue.svg)](https://github.com/lgruelas/finance/blob/master/LICENSE)

# Personal Finance Administrator

![Python master race](assets/python.png?raw=true "python")

## Getting started
This project has been made only for study porpouses, it allows you to administrate budgets for each category of your expenses, manage your accounts and so on, later on I might upload a demo video, for now it is under construction.

### Prerequisites
You must have a functional version of Node and npm, the frontend is working with React and the backend is Django.

### Installation

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


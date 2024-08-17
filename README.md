# Ocula Tech Exercise

This is a Ocula technical exercise

##  Technology Stack

It is actively developed using Python and the Django Framework.

Requires:

```
Docker
Postgres = 16.0
Python >= 3.10
Django ~= 5.0
```

## Development

This application can be developed in a Docker environment or virtual environment.

## Docker Environment

The application uses a docker PostgreSQL database instance.
Install the build prerequisites required to run psycopg2.

At the time of writing, the link below provides details to setup the required
build prerequisites: http://initd.org/psycopg/docs/install.html

You do not have to install the postgres client at system level.

To bring up the docker environment: `make up`
To bring down the docker environment: `make down`

## Virtual Environment

Create a virtual environment and install dependencies.

```
pip install -r requirements.txt
```

## Run Development Server

Even when running the app outside docker, you still need to run make up so the database is created.
Export environment variables:

```
export DATABASE_URL=postgres://postgres:postgres@localhost/ocula
export DJANGO_SETTINGS_MODULE=ocula.settings.local
```

Run the Django development server

Use python directly: `python manage.py runserver`

## Usage

To access the REST API: `http://localhost:8000/api/v1/temperature/?city=<city>&date=2024-08-16`

## Run Tests

Run the unit tests

Use python directly: `python manage.py test --parallel --failfast`

Run tests in a docker environment: `make test`

## Code QA

Install pre-commit: `pip install pre-commit`

pre-commit is used to run checks on the codebase before commits are made to git.

To run checks: `make check`

You can invoke pre-commit directly: `pre-commit run --all-files`

For more information: https://pre-commit.com/

## Manage Dependencies

pip-tools is used manage application dependencies
For more information: https://github.com/jazzband/pip-tools

Install pip-tools

```
pip install pip-tools
```

Add a new dependency to requirements.in and then run: `make requirements`

Upgrade dependencies

```
make upgrade-requirements
```

Sync dependencies in virtual environment to reflect upgrades

```
make sync-requirements
```

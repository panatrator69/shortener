# Shortener

Shortener is an HTTP web server that condenses a given URL into an alias. The outputted alias will redirect to the
original link.

### Pre-requisites

- Unix system (Mac or Linux)
- Python 3.12 or above
- Poetry python package manager
- Docker and docker-compose
- Pre Commit
- Git

### Starting The Server

Docker containers and images can be built and brought up with the `docker-compose` command.

```shell
docker-compose up
```

Alternatively, the `Makefile` with helper commands does the same thing.

```shell
make up
```

This will bring up the Postgres DB and FastAPI web service.

## Tests

Shortener uses `pytest` as its testing suite. Make sure it's installed with the `poetry` dev dependencies.

```shell
poetry install --group dev
```

### Running

Make sure the `postgres` container is up first

```
docker-compose up --detach
```

Run all tests with the following command:

```shell
poetry run pytest tests/
```

Or the Makefile equivalent

```shell
make test
```

## Pre-Commit Hooks

To install the pre-commit hooks with this repo, make sure you follow the installation instructions here first:
https://pre-commit.com/#installation

### Running manually

To run pre-commit hooks without a git commit, run the following command.

```shell
pre-commit run
```

Alternatively

```shell
make lint
```

This will run the hooks only on files that are changed from the current git `HEAD`.

To run pre-commit hooks on all files without a git command:

```shell
pre-commit run --all-files
```

or

```shell
make lint-all
```


## Features

- Shortened links will never expire
- Shortened links will have paths of 24 characters max.
- API will use JSON for request and response bodies.

## Installation



## Contributing


## License

[MIT](https://choosealicense.com/licenses/mit/)


## TODOs

- version pinning on Docker and poetry deps.
- Dockerfile copies necessary files over rather than the repo directory. To better mirror development vs production,
  consider using Dockerfile build stages.
- Create docker compose/Dockerfile for test container so that tests are ran deterministically.
- Reconsider using the primary id to encode the shortened link.
  - If there is a deletion of a row in the DB, then you'll have a shortened link that can never be reclaimed for use.
  - If a row is moved, then the primary id and the shortened link won't match up.
- Make sure to prefix the hostname to the shortened link.

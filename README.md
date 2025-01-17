# Shortener

Shortener is an HTTP web server writen in Python's `FastAPI` that provides link shortening and HTTP redirect
functionality.

## Getting Started

### Pre-requisites

- Unix system (Mac or Linux)
- Python 3.12 or above
- Poetry python package manager
- Docker and docker-compose
- Pre Commit
- Git

### The Makefile

A series of aliases for managing this package are defined in the `Makefile`. They can be invoked by:

```shell
make whatever-command
````

This README will use the `Makefile` commands. [Check the contents of the file](Makefile) for what's going on under the
hood.

### Installing

```shell
make build
```

This will build the Docker containers and install the poetry production and development dependencies to run the
pytest suite.

Run `make build-docker` or `make build-poetry` to build each component individually.

### Starting The Services

Bring up the web server and Postgres database. This will run `docker-compose up` and attach to the stdout streams.

```shell
make up
```

## Tests

Shortener uses pytest as its testing suite. Make sure it's installed with the poetry dev dependencies.

```shell
make build-poetry
```

Run all tests with the following command:

```shell
make test
```

## Pre-Commit Hooks

### Installing

```shell
make install-lint
```

### Running manually

To run pre-commit hooks without a git commit, run the following command.

```shell
make lint
```

This will run the hooks only on files that are changed from the current git `HEAD`.

To run pre-commit hooks on all files without a git commit:

```shell
make lint-all
```

### Skipping Hooks On Commit

If you're really having a disagreement with the hooks, or find some issue that just can't be resolved, the `-n` option
skips the pre commit hooks.

```shell
git commit -m "chore: example message" -n
```

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

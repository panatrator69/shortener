# Shortener

Shortener is an HTTP web server that condenses a given URL into an alias. The outputted alias will redirect to the 
original link.

## Features

- Shortened links will never expire
- Shortened links will have paths of 24 characters max.
- API will use JSON for request and response bodies.

## Installation

### Pre-requisites

- Unix system (Mac or Linux)
- Python 3.12 or above
- Poetry python package manager
- Docker and docker-compose


## Contributing


## License

[MIT](https://choosealicense.com/licenses/mit/)


## TODOs

- version pinning on Docker and poetry deps.
- Dockerfile copies necessary files over rather than the repo directory. To better mirror development vs production,
  consider using Dockerfile build stages.
- datetime create_now fields should probably be generated on the database side via a schema migration. 
  Not within the orm models.
- Need a precommit linter. Black or flake8 or something. I'm sick of manually ordering imports and chomping line length.
- TODO create docker compose/Dockerfile for test container so that tests are ran deterministically. 
build-docker:
	# Build docker images from docker-compose.yaml file.
	docker-compose build

build-poetry:
	poetry install --group dev

build: build-docker build-poetry


up:
	# Start all services
	docker-compose up

down:
	# Stop all services
	docker-compose down

clean:
	# Stop all services, Removes all containers. Deletes all images.
	docker-compose down --rmi all

	# Prunes all dangling images
	docker image prune

local-http-up:
	poetry run uvicorn shortener.app:app --host 0.0.0.0 --port 8000

install-lint:
	pre-commit install


lint-all:
	# Run precommit hooks on all files
	pre-commit run --all-files

lint:
	# Run pre commit hooks on files modified from HEAD
	pre-commit run

test:
	docker-compose up --detach
	poetry run pytest tests/

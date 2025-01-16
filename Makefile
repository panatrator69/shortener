local-http-up:
	poetry run uvicorn shortener.app:app --host 0.0.0.0 --port 8000

build:
	# Manually build the image outside of docker-compose
	docker build .

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

lint-all:
	# Run precommit hooks on all files
	pre-commit run --all-files

lint:
	pre-commit run

test:
	poetry run pytest tests/

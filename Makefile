http-up:
	poetry run uvicorn shortener.app:app --host 127.0.0.1 --port 8000

build:
	docker build .

FROM python:3.12.8-alpine3.21

RUN pip install poetry

# Don't copy entire git repo contents. Just
# the poetry config and app python files.
WORKDIR /app
COPY pyproject.toml poetry.lock ./
COPY shortener ./shortener
COPY README.md ./

# TODO How to install non dev depedencies.
RUN poetry install

ENTRYPOINT ["poetry", "run", "uvicorn", "shortener.app:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]

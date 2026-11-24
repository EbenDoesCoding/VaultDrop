PORT ?= 3000

.PHONY: install db test dev run down build clean

install:
	uv sync

db:
	docker compose up -d --wait db

test: db
	uv run pytest -v

dev:
	uv run uvicorn src.main:app --port $(PORT)

build:
	docker compose build

run:
	docker compose up --build

down:
	docker compose down

clean:
	find . -name '*.un~' -delete
	find . -name '__pycache__' -type d -exec rm -rf {} +
	rm -rf .pytest_cache

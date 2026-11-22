PORT ?= 3000
IMAGE ?= myapp

.PHONY: install test run clean docker-build docker-run compose-up compose-down

install:
	uv sync

test:
	uv run pytest -v
clean:
	find . -name '*.un~' -delete
	find . -name '__pycache__' -type d -exec rm -rf {} +
	rm -rf .pytest_cache
compose-up:
	docker compose up --build -d

compose-down:
	docker compose down

docker-build:
	docker build -t $(IMAGE) .

docker-run:
	docker run --rm -p $(PORT):3000 $(IMAGE)


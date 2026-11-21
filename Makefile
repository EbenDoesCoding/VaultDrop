PORT ?= 3000
IMAGE ?= myapp

.PHONY: install test run clean docker-build docker-run

install:
    uv sync

test:
	uv run pytest -v

run:
	uv run uvicorn src.main:app --port $(PORT)

clean:
	find . -name '*.un~' -delete
	find . -name '__pycache__' -type d -exec rm -rf {} +
	rm -rf .pytest_cache

docker-build:
    docker build -t $(IMAGE) .

docker-run:
    docker run --rm -p $(PORT):3000 $(IMAGE)

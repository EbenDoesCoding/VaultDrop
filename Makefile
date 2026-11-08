PORT ?= 3000

test:
	uv run pytest -v

run:
	uv run uvicorn src.main:app --port $(PORT)

clean:
	find . -name '*.un~' -delete
	find . -name '__pycache__' -type d -exec rm -rf {} +

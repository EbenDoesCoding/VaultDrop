.PHONY: build test run clean help

PORT ?= 3000

help:
	@echo "make build | test | run | clean   (PORT=$(PORT))"

build:
	@echo "TODO: install/build (e.g. npm ci, pip install -r requirements.txt)"

test: build
	@echo "TODO: wire real tests" && exit 1

run: build
	@echo "TODO: start service on port $(PORT)" && exit 1

clean:
	rm -rf node_modules coverage .nyc_output dist .venv __pycache__ .pytest_cache htmlcov
	find . -name '*un~' -delete

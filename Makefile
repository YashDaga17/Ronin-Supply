.PHONY: help install dev-install test lint format clean docker-up docker-down

help:
	@echo "Available commands:"
	@echo "  install      Install production dependencies"
	@echo "  dev-install  Install development dependencies"
	@echo "  test         Run tests"
	@echo "  lint         Run linting"
	@echo "  format       Format code"
	@echo "  clean        Clean up temporary files"
	@echo "  docker-up    Start Docker services"
	@echo "  docker-down  Stop Docker services"

install:
	pip install -r requirements.txt

dev-install:
	pip install -r requirements.txt
	pip install -e ".[dev]"

test:
	pytest

lint:
	flake8 ronin_supply tests
	mypy ronin_supply

format:
	black ronin_supply tests
	isort ronin_supply tests

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/

docker-up:
	docker-compose up -d postgres redis

docker-down:
	docker-compose down

docker-build:
	docker-compose build

run-dev:
	uvicorn ronin_supply.main:app --reload --host 0.0.0.0 --port 8000
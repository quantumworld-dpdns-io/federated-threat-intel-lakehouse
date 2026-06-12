.PHONY: install lint format typecheck test build clean all dev test-robot test-security test-quantum test-fl

install:
	pip install -e ".[all]" --quiet

install-dev:
	pip install -e ".[dev]" --quiet

install-test:
	pip install -e ".[test]" --quiet

install-quantum:
	pip install -e ".[quantum]" --quiet

install-fl:
	pip install -e ".[fl]" --quiet

lint:
	ruff check src/ tests/

format:
	ruff format src/ tests/

format-check:
	ruff format --check src/ tests/

typecheck:
	mypy src/

test:
	pytest tests/unit/ -v --tb=short

test-verbose:
	pytest tests/ -v --tb=long

test-cov:
	pytest tests/unit/ --cov=src --cov-report=term-missing --cov-report=html -v

test-integration:
	pytest tests/integration/ -v --tb=short -m integration

test-robot:
	python -m robot --loglevel DEBUG tests/robot/

test-security:
	python -m robot --loglevel DEBUG tests/robot/security/

test-quantum:
	pytest tests/unit/ -v --tb=short -m quantum

test-fl:
	pytest tests/unit/ -v --tb=short -m fl

test-e2e:
	pytest tests/integration/ -v --tb=long -m e2e

build:
	python -m build --wheel --sdist

clean:
	rm -rf dist/ build/ *.egg-info .mypy_cache .pytest_cache .ruff_cache htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

docker-up:
	docker compose up -d

docker-down:
	docker compose down -v

docker-build:
	docker compose build

docker-logs:
	docker compose logs -f

lint-all: lint typecheck format-check

all: clean lint typecheck test build

dev:
	uvicorn src.api.app:create_app --factory --reload --host 0.0.0.0 --port 8000

serve:
	uvicorn src.api.app:create_app --factory --host 0.0.0.0 --port 8000

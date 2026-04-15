.PHONY: help validate deploy run test lint clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

validate: ## Validate the DABs bundle
	DATABRICKS_BUNDLE_ENGINE=direct databricks bundle validate

deploy: validate ## Deploy pipeline to Databricks
	DATABRICKS_BUNDLE_ENGINE=direct databricks bundle deploy

run: ## Run the pipeline
	DATABRICKS_BUNDLE_ENGINE=direct databricks bundle run grocery_pipeline

test: ## Run BDD tests against deployed tables
	uv run behave --tags="@smoke"

test-all: ## Run all BDD tests
	uv run behave

lint: ## Lint Python sources
	uv run ruff check src/ features/
	uv run ruff format --check src/ features/

format: ## Auto-format Python sources
	uv run ruff format src/ features/

clean: ## Remove build artifacts
	rm -rf .databricks/ __pycache__ src/__pycache__ features/steps/__pycache__

gates: lint test ## Run all quality gates before shipping

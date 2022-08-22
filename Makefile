
.PHONY: run format lint traceback db


run:
	@python mankey/main.py

rm:
	@rm mankey/data/personal_data/.env

format:
	@black --line-length 79 .
	@isort .

lint:
	@echo "FLAKE8:"
	@flake8 * --exclude Makefile || true
	@echo "PYDOCSTYLE:"
	@pydocstyle * || true

db:
	@python mankey/data/db.py


PROJECT_DIR := $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

init:
	@echo "Project dir is $(PROJECT_DIR)."

install-prerequesites:	init
	@pip install -r requirements.txt -r requirements-test.txt -r requirements-dev.txt

tests:	init
	@echo "Running tests..."; \
	PYTHONPATH=$(PROJECT_DIR) python -m unittest discover -s $(PROJECT_DIR) -v -p '*_test.py'

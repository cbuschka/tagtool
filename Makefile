PROJECT_DIR := $(dir $(realpath $(firstword $(MAKEFILE_LIST))))
SRC_DIR := $(PROJECT_DIR)/src

init:
	@echo "Project dir is $(PROJECT_DIR)."

install-prerequesites:	init
	@pip install -r requirements.txt -r requirements-test.txt -r requirements-dev.txt

tests:	init
	@echo "Running tests..."; \
	PYTHONPATH=$(SRC_DIR) python -B -m unittest discover -s $(SRC_DIR) -v -p '*_test.py'

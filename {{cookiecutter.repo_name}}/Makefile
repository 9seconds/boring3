ROOT_DIR    := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

PIP_COMPILE := pip-compile --generate-hashes --no-index --emit-trusted-host --rebuild --annotate --upgrade

# ---------------------------------------------------------------------------------------------------------------------

update-requirements:
	$(PIP_COMPILE) --output-file optional-requirements.txt optional-requirements.in && \
	$(PIP_COMPILE) --output-file test-requirements.txt test-requirements.in && \
	$(PIP_COMPILE) --output-file requirements.txt -U setup.py

install-requirements:
	pip install -r optional-requirements.txt -r test-requirements.txt -r requirements.txt

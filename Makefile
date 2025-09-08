PHONY: clean setup activate test
SHELL := /bin/bash

clean:
	rm -rf __pycache__ */__pycache__

venv:
	python -m venv venv

setup: venv
	$(MAKE) activate
	pip install -r requirements.txt

activate:
	source venv/bin/activate

test:
	$(MAKE) activate
	python -m unittest test/*py

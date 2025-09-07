PHONY: clean setup activate test
SHELL := /bin/bash

clean:
	rm -rf __pycache__ */__pycache__

setup:
	python -m venv venv
	make activate
	pip install -r requirements.txt

activate:
	source venv/bin/activate

test:
	make activate
	python -m unittest test/*py

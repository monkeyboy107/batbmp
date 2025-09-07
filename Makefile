.PHONY: clean setup activate test
SHELL := /bin/bash
V = source venv/bin/activate;

clean:
	rm -rf __pycache__ */__pycache__

venv:
	python -m venv venv

setup: venv
	$(V) pip install -r requirements.txt

test: venv
	$(V) python -m unittest test/*py

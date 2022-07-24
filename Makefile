setup: requirements-dev.txt
	python -m venv .venv 
	. .venv/bin/activate 
	pip install -r requirements-dev.tx
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .venv
pytest:
	. .venv/bin/activate
	python -m pytest --capture=no
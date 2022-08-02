setup: requirements-dev.txt
	python -m venv .venv
	pip install -r requirements-dev.txt

clean:
	rm -rf __pycache__
	rm -rf .venv/
setup: requirements.txt
	python -m venv .venv
	pip install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf .venv/
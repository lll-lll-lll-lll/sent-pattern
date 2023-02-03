setup: requirements.txt
	python -m venv .dev-venv
	pip install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf .venv/
	rm -rf build
	rm -rf dist
	rm -rf sent_pattern.egg-info/
	rm -rf .pytest_cache/

build:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

upload:
	twine upload --repository pypi dist/*
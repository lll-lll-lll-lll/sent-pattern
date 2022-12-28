setup: requirements.txt
	python -m venv .dev-venv
	pip install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf .venv/
	rm -rf build
	rm -rf dist

build:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

upload:
	twine upload --repository pypi dist/*
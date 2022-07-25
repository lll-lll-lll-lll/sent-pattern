.PHONY: setup
setup:
	poetry install --no-dev
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
pytest:
	poetry run pytest --capture=no

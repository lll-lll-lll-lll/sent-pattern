.PHONY: setup
setup:
	poetry install
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
pytest:
	poetry run pytest --capture=no

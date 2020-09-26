configure:
	poetry install

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

test:
	pytest --cov-report xml --cov=tests/

publish:
	poetry publish -r testpypi
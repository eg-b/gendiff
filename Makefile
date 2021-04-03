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
	poetry run pytest --cov=gendiff tests/ --cov-report xml

publish:
	poetry publish -r testpypi

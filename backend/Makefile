default: start

start:
	$(info )
	$(info -- Starting server --)
	$(info )
	.venv/bin/python3 manage.py runserver

celery:
	$(info )
	$(info -- Starting Celery --)
	$(info )
	celery -A climateconnect_main worker -l INFO

celery_beat:
	$(info )
	$(info -- Starting Celery Beat --)
	$(info )
	celery -A climateconnect_main beat -l INFO

shell:
	.venv/bin/python3 manage.py shell

install:
	pdm install

test:
	.venv/bin/python3 manage.py test

docker:
	docker-compose up -d
	$(info )
	$(info -- Running Docker in background (detached mode) --)
	$(info )

all: docker start

# Note: this should be in sync with out CI GitHub action that lints too. See
# those files under .github/workflows
lint:
	flake8 . --count --select=E9,F6,F7,F8 --show-source --statistics

format:
	black .

# Database migrations and test data creation:
migrate:
	.venv/bin/python3 manage.py migrate

migrations: migrate

test-data:
	.venv/bin/python3 manage.py create_test_data --number_of_rows 4

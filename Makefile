install: 
	poetry install --no dev 

install-dev: 
	poetry install 

serve:
	uvicorn app.main:app --reload

migrations:
	alembic revision --autogenerate -m "latest"

build:
	alembic upgrade head

test:
	bash scripts/test.sh

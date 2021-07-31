install: 
	poetry install 

serve:
	uvicorn app.main:app --reload

build:
	alembic revision --autogenerate -m "latest"

test:
	bash scripts/test.sh

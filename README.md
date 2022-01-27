## FastAPI template project

This is a condensed version of the fastapi cookier cutter found [here](https://github.com/tiangolo/full-stack-fastapi-postgresql)

This is intended to be the minimum necessary to start building a larger project with no opinion on deployment or databases

### Installation
Install poetry and packages
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
make install
```


## Development
Install development version
```
make install-dev
```
### Create a database 
```
create database fastapi_db;
create user thatsyou with password 'changethis';
ALTER ROLE thatsyou SET client_encoding TO 'utf8';
ALTER ROLE thatsyou SET default_transaction_isolation TO 'read committed';
ALTER ROLE thatsyou SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE fastapi_db to thatsyou;
```

### Set the environment variables
```
export POSTGRES_SERVER="localhost"
export POSTGRES_USER="thatsyou"
export POSTGRES_PASSWORD="changethis"
export POSTGRES_DB="fastapi_db"
export POSTGRES_TEST_DB="nameoftestdatabase"
```

### Create the database migration
```
alembic revision --autogenerate -m "initial revision"
```

### Run the migrations to update the tables in the database
```
alembic upgrade head
```
### Check the installation

```
make test
```

Serve the application
```
make serve
```


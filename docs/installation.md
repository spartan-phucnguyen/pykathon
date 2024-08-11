## Run project in Pycharm

- Set environment variable `ENVIRONMENT=local`, the file `config.local.yaml` will be
  effected. For production, we will use `config.local` instead
- Environment variable convention:
    - By
      following [pydantic parsing environment](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#parsing-environment-variable-values)
      document, use `__` for nested delimiter.
    - For example: `POSTGRES__DB_NAME=new_db_name` will
      replace `{"postgres":{"db_name":"local"}}`
- Apply & Run

## Configure Interpreter

1. Click 'Python Interpreter'
2. Choose "Add New Interpreter" -> "Add Local Interpreter..."
3. Choose "Poetry Environment" -> Click "Poetry Environment"
4. At "Base interpreter" click dropdown and choose interpreter suitable.
5. Click "OK"

### Note: If you use vscode, please follow these steps to install Python venv

```shell
python3 -m venv .venv
source .venv/bin/active
```

## Flyway

Add the flyway.conf to sql folder

```text
flyway.url=jdbc:postgresql://localhost:5432/service_platform
flyway.user=local
flyway.password=local
flyway.locations=filesystem:./
flyway.sqlMigrationPrefix=V
flyway.sqlMigrationSeparator=__
flyway.table=schema_version
flyway.cleanDisabled=false
```

Flyway migrate

```shell
cd __sql__ && flyway migrate && cd -
```

Flyway clean & migrate:

```shell
cd __sql__ && flyway clean migrate && cd -
```

## Poetry

This project uses poetry. It's a modern dependency management tool.

To run the project use this set of commands:

```bash
poetry install
```

If we have a problem with `openssl` is already installed

```shell
export PYCURL_SSL_LIBRARY=openssl
export LDFLAGS=-L/opt/homebrew/Cellar/openssl@3/3.3.0/lib
export CPPFLAGS=-I/opt/homebrew/Cellar/openssl@3/3.3.0/include
```

Start the application

```shell
python -m service_platform
```

## Pre-commit

To install pre-commit simply run inside the shell:

```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:

* ruff
* pytest

You can read more about pre-commit here: https://pre-commit.com/

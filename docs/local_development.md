## Local development

### Requisites

- Python: `^3.12`
- Poetry

### Managing environment with `Poetry`

You can use the env use command to tell Poetry which Python version to use for the
current project.

```shell
poetry env use /full/path/to/python
```

If you have the python executable in your PATH you can use it:

```shell
poetry env use python3.7
```

### Run project

- Install dependencies:

```shell
poetry install
```

- Start the application

```shell
python -m service_platform
```

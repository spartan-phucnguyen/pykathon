# service_platform

----
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://docs.pydantic.dev/latest/contributing/#badges)

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)]()

This is a template project for a python microservice using FastAPI framework.
Python 3.12 recommended.

## Structure

```shell
.
├── Dockerfile.migration
├── poetry.lock
├── pyproject.toml
├── docs
├── src
│    ├── service_platform
│    │   ├── api
│    │   │   ├── controller
│    │   │   │   ├── auth
│    │   │   │   ├── health
│    │   │   │   └── user
│    │   │   ├── exception
│    │   │   └── manager
│    │   │       ├── auth
│    │   │       └── user
│    │   ├── client
│    │   │   ├── auth0
│    │   │   ├── google
│    │   │   ├── health
│    │   │   ├── linkedin
│    │   │   ├── model
│    │   │   ├── request
│    │   │   │   ├── auth
│    │   │   │   └── user
│    │   │   ├── response
│    │   │   │   ├── auth
│    │   │   │   └── user
│    │   │   └── zoom
│    │   ├── core
│    │   │   ├── errors
│    │   │   ├── middleware
│    │   │   ├── repository
│    │   │   ├── response
│    │   │   └── security
│    │   ├── db
│    │   │   ├── __sql__
│    │   │   ├── refresh_token
│    │   │   └── user
│    │   ├── k8s
│    │   │   └── dev
│    │   ├── runtime
│    │   │   └── settings
│    │   ├── service
│    │   │   ├── auth0
│    │   │   │   └── oauth
│    │   │   ├── aws
│    │   │   │   ├── s3
│    │   │   │   └── sqs
│    │   │   ├── google
│    │   │   │   └── oauth
│    │   │   ├── linkedin
│    │   │   │   └── oauth
│    │   │   ├── postgres
│    │   │   ├── redis
│    │   │   └── zoom
│    │   │       └── oauth
│    │   ├── utils
│    │   │   └── logging
│    │   └── worker
│    │       └── example_worker
│    │           ├── consumer
│    │           ├── processor
│    │           └── repository
│    └── tools
│        └── commands
│            └── templates
└── tests
    └── api

```

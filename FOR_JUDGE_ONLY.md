# API Template for c0x12c hackathon

-----

## What we did in advances

### Refactor codebase

#### Why?

- Current codebase is unstructured => hard for look up something in a domain

#### Solution

- We leverage the domain driven architect, we want to separate the configuration with
  its usage, we separate service_platform with tools (which is only useful for dev).

### Added Formating

#### Why?

- A nonstandard formatting will bring new developers most of the toughs and very hard to
  maintain, its very ugly and bring a huge stress for reader.

#### Solution

- Installed `ruff`, added ruff check in `pre-commit` hooks

### Statical Type Analysis

#### Why?

- Python is dynamic typing which is a double-edge sword. It can fast for development but
  will cause a terrible performance

#### Solution

- Installed `mypy` as a dev dependency, also added the IDE plugins for static type
  check. It can check for valid or invalid type while you are typing, it's very
  convenient.
- `mypy` also provide us a CLI to check manually, we take advantages of this to leverage
  the `pre-commit` hooks of GitHub.

### Command for basic CRUD:

#### Why?

- The FastAPI template is quite complex for engineers who haven't worked with FastAPI (
  Python) before and can be tedious for engineers already familiar with it.

#### Solution

- Quickly generate basic CRUD: `controller`, `repository` via Command (Inspired by
  Laravel)
    + Repository: ./fastapi create_repository [name] (ex: ./fastapi
      create_repository product)
    + Controller: ./fastapi create_controller [name]

- Use inflect to handle Singular & Plural case

## What are some challenges we have faced when we develop this template?

1. Huge amount of typing error: after installed `mypy` for type check, we almost fainted
   because of the massive error. We spent most of the time just by fixing the type, but
   some error comes from third party error, we can't address them in a period, so we
   decided to skip for some files. It's not a great choice but we need to do it to get
   the sh*t done.
2.

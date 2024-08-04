import typer
import os
import inflect

app = typer.Typer()
p = inflect.engine()

@app.command()
def hello(txt: str):
    print(f'HELLO {txt}')

@app.command(name='create_controller')
def create_controller(name: str):
    # Define directories and file paths
    controller_base_directory = f'src/service_platform/api/controller/{name}'
    manager_base_directory = f'src/service_platform/api/manager/{name}'
    controller_file_path = os.path.join(controller_base_directory, 'route.py')
    manager_file_path = os.path.join(manager_base_directory, 'manager.py')
    response_file_path = os.path.join(manager_base_directory, 'response.py')
    schema_file_path = os.path.join(controller_base_directory, 'schema.py')
    init_controller_file_path = os.path.join(controller_base_directory, '__init__.py')
    init_manager_file_path = os.path.join(manager_base_directory, '__init__.py')

    # Create directories if they don't exist
    os.makedirs(controller_base_directory, exist_ok=True)
    os.makedirs(manager_base_directory, exist_ok=True)

    # Check if the files already exist
    if os.path.exists(controller_file_path):
        typer.echo(f'Controller {name} already exists.')
        raise typer.Exit()
    if os.path.exists(manager_file_path):
        typer.echo(f'Manager {name} already exists.')
        raise typer.Exit()

    # Create the controller file with a basic template
    with open(controller_file_path, 'w') as f:
        f.write(f'''import uuid
from typing import Annotated, List

from fastapi import APIRouter, Depends, Body

router = APIRouter()

@class_router(router)
class {name.capitalize()}Router:
    def __init__(self, {name}_manager: {name.capitalize()}Manager = Depends()):
        self.manager = {name}_manager

    @router.post("/{name}/create")
    async def create_{name}(
        self,
        token_data: Annotated[TokenData, Depends(get_token_data)],
        payload: Create{name.capitalize()}Request = Body(Create{name.capitalize()}Request),
    ) -> {name.capitalize()}Response:
        return await self.manager.create_{name}(
            user_id=token_data.user_id,
            payload=payload,
        )

    @router.post("/{name}/update")
    async def update_{name}(
        self,
        {name}_id: uuid.UUID,
        payload: Update{name.capitalize()}Request = Body(Update{name.capitalize()}Request),
    ) -> MessageResponse:
        return await self.manager.update_{name}(
            {name}_id={name}_id, payload=payload
        )

    @router.post("/{name}/delete")
    async def delete_{name}(
        self,
        {name}_id: uuid.UUID,
    ) -> MessageResponse:
        return await self.manager.delete_{name}({name}_id)
''')

    # Create the manager file with a basic template
    with open(manager_file_path, 'w') as f:
        f.write(f'''from typing import List

class {name.capitalize()}Manager:
    async def create_{name}(self, user_id: str, payload: Create{name.capitalize()}Request) -> {name.capitalize()}Response:
        # Implement the logic to create a {name}
        pass

    async def update_{name}(self, {name}_id: uuid.UUID, payload: Update{name.capitalize()}Request) -> MessageResponse:
        # Implement the logic to update a {name}
        pass

    async def delete_{name}(self, {name}_id: uuid.UUID) -> MessageResponse:
        # Implement the logic to delete a {name}
        pass
''')

    # Create the response file with a basic template
    with open(response_file_path, 'w') as f:
        f.write(f'''from __future__ import annotations

from typing import List

from service_platform.api.controller.{name}.schema import (
    {name.capitalize()}Response,
)

from service_platform.db.{name}.table import {name.capitalize()}Entity

class {name.capitalize()}ResponseConverter:
    def to_{name}_response(
        self,
        {name}: {name.capitalize()}Entity,
    ) -> {name.capitalize()}Response:
        return {name.capitalize()}Response(
            id={name}.id,
            name={name}.name,
        )

    def to_{name}s_response(self, {name}s: List[{name.capitalize()}Entity]) -> List[{name.capitalize()}Response]:
        return [self.to_{name}_response(fol) for fol in {name}s]
''')

    # Create the schema file with a basic template
    with open(schema_file_path, 'w') as f:
        f.write(f'''from __future__ import annotations

import uuid
from datetime import datetime
from typing import List

from service_platform.core.base_schema import CoreModel

class Create{name.capitalize()}Request(CoreModel):
    name: str

class Update{name.capitalize()}Request(CoreModel):
    name: str | None = None

class {name.capitalize()}Response(CoreModel):
    id: uuid.UUID
    name: str
''')

    # Create the __init__.py file for controller
    with open(init_controller_file_path, 'w') as f:
        f.write('')

    # Create the __init__.py file for manager
    with open(init_manager_file_path, 'w') as f:
        f.write('')

    typer.echo(f'Controller {name} created successfully at {controller_file_path}.')
    typer.echo(f'Manager {name} created successfully at {manager_file_path}.')
    typer.echo(f'Response {name} created successfully at {response_file_path}.')

@app.command(name='create_repository')
def create_repository(name: str):
    # Define directories and file paths
    entity_base_directory = f'src/service_platform/db/{name}'
    entity_file_path = os.path.join(entity_base_directory, 'table.py')
    repository_file_path = os.path.join(entity_base_directory, 'repository.py')
    init_entity_file_path = os.path.join(entity_base_directory, '__init__.py')

    # Create directories if they don't exist
    os.makedirs(entity_base_directory, exist_ok=True)

    # Check if the files already exist
    if os.path.exists(entity_file_path):
        typer.echo(f'Entity {name} already exists.')
        raise typer.Exit()
    if os.path.exists(repository_file_path):
        typer.echo(f'Repository {name} already exists.')
        raise typer.Exit()

    # Pluralize the entity name
    plural_name = p.plural(name)

    # Create the entity file with a basic template
    with open(entity_file_path, 'w') as f:
        f.write(f'''from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from service_platform.db.base_class import Base
import uuid

class {name.capitalize()}Entity(Base):
    __tablename__ = '{plural_name}'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
''')

    # Create the repository file with a basic template
    with open(repository_file_path, 'w') as f:
        f.write(f'''from sqlalchemy.orm import Session
from service_platform.db.{name}.table import {name.capitalize()}Entity

class {name.capitalize()}Repository:
    def __init__(self, db: Session):
        self.db = db

    def get_{name}(self, {name}_id: str) -> {name.capitalize()}Entity:
        return self.db.query({name.capitalize()}Entity).filter({name.capitalize()}Entity.id == {name}_id).first()

    def create_{name}(self, {name}: {name.capitalize()}Entity) -> {name.capitalize()}Entity:
        self.db.add({name})
        self.db.commit()
        self.db.refresh({name})
        return {name}

    def update_{name}(self, {name}: {name.capitalize()}Entity) -> {name.capitalize()}Entity:
        self.db.merge({name})
        self.db.commit()
        return {name}

    def delete_{name}(self, {name}_id: str) -> None:
        {name} = self.db.query({name.capitalize()}Entity).filter({name.capitalize()}Entity.id == {name}_id).first()
        if {name}:
            self.db.delete({name})
            self.db.commit()
''')

    # Create the __init__.py file for entity and repository
    with open(init_entity_file_path, 'w') as f:
        f.write('')

    typer.echo(f'Entity and Repository {name} created successfully at {entity_file_path} and {repository_file_path}.')

if __name__ == "__main__":
    app()

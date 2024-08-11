import typer
import os
import inflect

app = typer.Typer()
p = inflect.engine()

def read_template(template_path: str) -> str:
    if not os.path.exists(template_path):
        typer.echo(f"Template file not found: {template_path}")
        raise FileNotFoundError(f"Template file not found: {template_path}")
    with open(template_path, 'r') as file:
        return file.read()

@app.command(name='create_controller')
def create_controller(name: str):
    # Debug: Print current working directory
    typer.echo(f"Current working directory: {os.getcwd()}")

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

    # Read templates
    controller_template = read_template('src/service_platform/command/templates/controller_template.py')
    manager_template = read_template('src/service_platform/command/templates/manager_template.py')
    response_template = read_template('src/service_platform/command/templates/response_template.py')
    schema_template = read_template('src/service_platform/command/templates/schema_template.py')

    # Create the controller file with a basic template
    with open(controller_file_path, 'w') as f:
        f.write(controller_template.format(name=name.capitalize(), name_lower=name.lower()))

    # Create the manager file with a basic template
    with open(manager_file_path, 'w') as f:
        f.write(manager_template.format(name=name.capitalize(), name_lower=name.lower()))

    # Create the response file with a basic template
    with open(response_file_path, 'w') as f:
        f.write(response_template.format(name=name.capitalize(), name_lower=name.lower()))

    # Create the schema file with a basic template
    with open(schema_file_path, 'w') as f:
        f.write(schema_template.format(name=name.capitalize()))

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
    # Debug: Print current working directory
    typer.echo(f"Current working directory: {os.getcwd()}")

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

    # Read templates
    entity_template = read_template('src/service_platform/command/templates/entity_template.py')
    repository_template = read_template('src/service_platform/command/templates/repository_template.py')

    # Create the entity file with a basic template
    with open(entity_file_path, 'w') as f:
        f.write(entity_template.format(name=name.capitalize(), plural_name=plural_name))

    # Create the repository file with a basic template
    with open(repository_file_path, 'w') as f:
        f.write(repository_template.format(name=name.capitalize(), name_lower=name.lower()))

    # Create the __init__.py file for entity and repository
    with open(init_entity_file_path, 'w') as f:
        f.write('')

    typer.echo(f'Entity and Repository {name} created successfully at {entity_file_path} and {repository_file_path}.')

if __name__ == "__main__":
    app()

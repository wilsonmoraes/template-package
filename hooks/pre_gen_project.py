import os
from cookiecutter.main import cookiecutter

path = os.getcwd()

root_directory = os.path.dirname(path)

cookiecutter('git@github.com:wilsonmoraes/template-package.git',
             extra_context={'project': root_directory})


def validate_empty_fields(data, field):
    if not data:
        print(f"ERROR: '{data}' is not a valid {field}!")
        sys.exit(1)


validate_empty_fields('{{ cookiecutter.project_short_description }}', "project_short_description")

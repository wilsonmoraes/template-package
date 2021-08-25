{{ "{!s:=>%s}".__mod__(cookiecutter.project.__len__()).format("") }}
{{ cookiecutter.project }}
{{ "{!s:=>%s}".__mod__(cookiecutter.project.__len__()).format("") }}
{# The hack above generate a line with '=' with len(cookiecutter.project) size #}

{{ cookiecutter.project_short_description }}


Local installation and configuration
------------------------------------

To install the project for development just use:

.. code::

  poetry install




-----------------

Based on template: {{ cookiecutter._template_version }}

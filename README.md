# Cookiecutter Python Package Generator

<div align="left">

[![Build status](https://github.com/TezRomacH/python-package-template/workflows/build/badge.svg?branch=master&event=push)](https://github.com/TezRomacH/python-package-template/actions?query=workflow%3Abuild)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/TezRomacH/python-package-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/TezRomacH/python-package-template/releases)
[![License](https://img.shields.io/github/license/TezRomacH/python-package-template)](https://github.com/TezRomacH/python-package-template/blob/master/LICENSE)

Your next Python package needs a ideal project structure.
</div>


## Requirements
> All you need is the latest version of cookiecutter 😉
* [Python 3.7+](https://python.org)
* [cookiecutter 1.3+](https://cookiecutter.readthedocs.org/en/latest/)



## 🤯 How to use it

### Installation

To begin using the template consider updating `cookiecutter`

```bash
pip install -U cookiecutter
```

Then go to a directory where you want to create your project and run:

```bash
cookiecutter git@github.com:wilsonmoraes/template-package.git
```

### Input variables

Template generator will ask you to fill some variables.

The input variables, with their default values:


|     **Parameter**     |      **Required**      |      **Default value**      |  **Description**                                                                                                                                                               |
|:---------------------:|:---------------------------:|:---------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project`           | `True`            |             | Check the availability of possible name  before creating the project. |
| `repo_name`           |             |      based on the `organization`       | GitHub username for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for GitHub. |
| `project_short_description`           |     `True`        |          | Brief description of your project. |

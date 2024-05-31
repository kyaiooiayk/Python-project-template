# 🐍📝Template for your Python project🐍📝
- This repo is a template with explanations. An initial explanation is provided and links are offered for the curious.
- The real template which can be copied is located under the `template` folder.
- The python scripts contains mostly OOP codes. This should serves as a concrete example of production codes.
***

## Environment vs. package managers
- You have 3 options and admitally their goals overlaps quite a lot:
    - Python native
    - `Pyenv`
    - `conda`: very robust package environment manager not limited to python.
    - `poetry`: best choice for production package manager. This boils down to the fact it is very good at managing dependency requirements and conflict.
- Check [this](https://github.com/kyaiooiayk/Environment-Package-and-Project-Manager/blob/dev/README.md) out if you want to know more about the differences between the three and how to install poetry.
***

## Module vs. packages
- **module** – a module is a file containing Python functions.
- **package** – a package is a collection of modules intended to be installed and used together. Packages are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name `A.B` designates a submodule named `B` in a package named `A`. 
- This template focuses on how to build a package.
   A module is simply a file containing Python code. A package, however, is like a directory that holds sub-packages and modules. In order for a package to be importable, it should contain a `__init__.py` file. That’s not the case for modules.
- [Module vs. Package vs. Library vs. Framework](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/modules_packages_libraries_frameworks.md)
***

## GitHub in the big picture
Generally a good DS and most definetly a ML/MLOPS will generally follow the following steps:
- `poetry`: sort out virtual environments for good, all your project definitions in pyproject.toml. Much better than conda and virtual env.
- `black`: code formatte
- `ruff`: new blazing fast linter, anything that black doesn't care about will be fixed here
- `pytest`: test your code
- `pre-commit-hooks`: automate all of the above and forget about them.    
- **GitHub Actions: run these on the remote as well, just to be sure.**
```shell
poetry new -n --src <project>
cd <project>
poetry config virtualenvs.in-project true
poetry env use python3.10
source .venv/bin/activate
poetry add back ruff pytest pre-commit
git init
git add .
git commit -m "my first commit"
git branch -M main
git remote add origin git@github.com:<username>/<project>.git # Create empty repositore on remote server
git push -u origin main
pre-commit install
poetry run pytest
poetry run black .
poetry run ruff . --fix
```
***

## Overview
| What | Location | Purpouse | Find out more|
| :-: | :-: | :-: | :-: |
| `LICENSE` | `root` | Telling users/contributors what they can/can't use the package for | |
| `setup.py` | `root` | Package and distribution management | |
| `requirements.txt` | `root` | List of dependencies for users | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/requirements.md) |
| `requirements-dev.txt` | `root` | List of dependencies for developers | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/requirements.md) |
| `docs` | `root/docs` | Package info, API descriptios and tutorials | |
| `tests` | `root/tests`| Intergration and unittests | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/tree/main/tutorials/Testing) |
| `context.py` | `root/tests` | Facilitate tests without installing the package |
| `Makefile` | `root` | Generic management tasks | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/tree/main/tutorials/makefile) |
| `__init__.py` | `root/src/package_name` | Required so you can import the directory as a package, and is generally empty ot set the `__all__` variable  | [Tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/self%20and%20__init__.ipynb) |
| `pyproject.toml` | `root` | Managed by poetry if you used, but still editable by you | [Tutorial](https://github.com/kyaiooiayk/Environment-Package-and-Project-Manager/blob/dev/README.md) |
| `pyproject.lock` | `root` | Managed by poetry if you used, but still editable by you. It stores only the metadata of dependencies that do not have conflicts with one another.  | [Tutorial](https://github.com/kyaiooiayk/Environment-Package-and-Project-Manager/blob/dev/README.md) |
***

## What to put in your project
***

### The `test` folder
- The test folder go at the top-level of the project with an `__init__.py` file so they are discoverable by applications like `pytest`.
- The alternative of placing them inside the src/mypackage directory means they will get deployed into production which may not be desirable.
- Tests need to import your packaged module to test it. You have two options:
    - Expect the package to be installed in site-packages.
    - Use a simple (but explicit) path modification to resolve the package properly.
- The latter is recommended. Requiring a developer to run setup.py develop to test an actively changing codebase also requires them to have an isolated environment setup for each instance of the codebase.
- To give the individual tests import context, create a `tests/context.py` file:
```python
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'path_to_your_package')))

import your_package_name
```
- Then, within the individual test modules, import the module like so: `from context import sample`
- This will always work as expected, regardless of installation method.

### The `src` folder
- It prevents tools like pytest incidently importing it.

### The `docs` folder
- Package reference documentation.
***

### The `Setup.cfg` file
- This file is no longer required for configuring a package, but third-party tools may still use it. 

### The `pyproject.toml` file
- This is what replaces `setup.cfg`.

### `setup.py` file
- The setup file dictates everything Python installer needs to know when building/publicising your package.
- It is also important to note (although this is mixed up), `setup.py` is NOT required for installation, but only for build/publication.
- Once it is written, two things needs to be *continously* updated:
    - Version
    - Install requirements
- The minimal `setup.py` file looks like this:
```python
from setuptools import setup

if __name__ == "__main__":
    setup()
```
- If you do not intend to publish your project then this file is NOT required at all, and `pip install -e .` will still work. `e` stands for `editable`. Upon execution you should be able to see something like this:
```shell
Successfully built my-package-name
Installing collected packages: my-package-name
Successfully installed my-package-name-0.0.0
```
- Now you can import the package with: `import my_package_name`
- This will add a symlink into your site-packages folder and make your local project behave as if it was fully installed while at the same time you can continue editing. This saves you from adding this at the to of the file:
```python
import sys
sys.path.append("../")
```
### `requirements.txt` & `requirements-dev.txt`
- It should specify the dependencies required.
- Check this out [how to generate a requirements.txt](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/requirements.md) if you want to know more.
- Generally, it is good practice to keep to file, one for normal usage and one for development where you can you put the requiremetns for testing, building, and generating documentation.
- This file is not requied if (generally people put both options):
    - There are no dependencies.
    - There is a preference to set up the environment via `setup.py`.
- If you are using poetry these files are not required as they managed automatically for you:
```shell
[tool.poetry.dependencies]
numpy = "^1.22.3"
pandas = "^1.4.2"

[tool.poetry.dev-dependencies]
black = "^21.7b0"
isort = "^5.9.3"
pytest = "^6.0"
```

### `Makefile`
- It is used to executing generic tasks for your project.
- Pay attention that to be valid it needs to have a particular formatting.
- Check [this](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/tree/main/tutorials/makefile/example_1) to find out more.
```Makefile
init:
    pip install -r requirements.txt

test:
    py.test tests

.PHONY: init test
```
***

###  `README.md`
- Your project front page.

###  `LICENSE`
- This is where, the full license text and copyright claims should exist in this file. If unsture, check out [choosealicense.com](https://choosealicense.com/).
- You are also free to publish code without a license, but this would prevent many people from potentially using or contributing to your code.
***

## How to deploy your doc with GitHub pages
- This is probably the easiest option available out there.
- Install `mkdocs` with: `pip install mkdocs`
- Create a folder called docs in your repository and place there all the `.md` files there.
- Create a `mkdocs.ymal` on your project root directory.
- Build doctumentation with: `mkdocs buil`
- Build doctumentation with: `mkdocs` serve and you can have a look at the locally deployed docs.
- When you are satisfied with it, you can then deploy it to Github pages with: `mkdocs gh-deploy`. This will create an additional branch called gh-pages and your docs should then be available.
***

## How to deploy the package in PyPI
- Go to pypi.org and create an account
- Install twine with: `pip install twine`
- Next, we’ll create an installable package. Go to the directory where the setup.py file is, and run: `python setup.py sdist bdist_wheel`. This creates `dist` and `your_package.egg-info`. The former is what we'll deploy in PyPI.
- Make sure your `.gitignore` is update otherwise this installation files will be pushed to the repo.
- Verify the distribution files you just created are okay by running: `twine check dist/*`
- Deploy first to the PyPI test domain with: `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
- Go to test.pypi.org and check your new library.
- Push it to the real PyPI: `twine upload dist/*`
- This can all be automated with the following shell script called build_deply.sh (`./build_deploy.sh` or `./build_deploy.sh --test`).
- Make the script executable with: `chmod +x build_deploy.sh`
```shell
rm -r dist ;
python setup.py sdist bdist_wheel ;
if twine check dist/* ; then
  if [ "$1" = "--test" ] ; then
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
  else
    twine upload dist/* ;
  fi
fi
```
- See [this](https://pypistats.org/search/pyde) if you want to see some statistics about your package.
***

## What you can run manually
- Many of the checks (formatting, linting, etc.. ) can be run through a `.pre-commit.ymal` which is triggered by some evernts.
- This can be overwritten in two ways:
    - Run the pre-commit with `pre-commit run -a`
    - Run one tool of you choice: `black file.py` or `flake file.py` or `pylint`
***

## References
- [How to build your first python package](https://towardsdatascience.com/how-to-build-your-first-python-package-6a00b02635c9)
- [Publishing packages and modules](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
- [Understanding setup.py, setup.cfg and pyproject.toml in Python](https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/)
- [Avoiding `sys.path.append(..)` for imports](https://stackoverflow.com/questions/68033795/avoiding-sys-path-append-for-imports)
- [Packaging a Python Codebase](https://madewithml.com/courses/mlops/packaging/)
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [python-package-template](https://github.com/TezRomacH/python-package-template)
- [Structuring Your Project](https://docs.python-guide.org/writing/structure/)
- [Packaging project](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
***

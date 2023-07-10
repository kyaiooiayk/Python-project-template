# 🐍📝Template for your Python project🐍📝
- This repo is a template with explanation.
- The real tamplate which can be copy is located under the `template` folder.
***

## Module vs. packages
- **module** – a module is a file containing Python functions.
- **package** – a package is a collection of modules intended to be installed and used together.
- This templates focuses on you to build a package.
- [Module vs. Package vs. Library vs. Framework](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/modules_packages_libraries_frameworks.md)
***

## Overview
| What | Location | Purpouse | Find out more|
| :-: | :-: | :-: |
| `LICENSE` | `root` | Telling users/contributor what they can/can't use the package for |
| `setup.py` | `root` | Package and distribution management |
| `requirements.txt` | `root` | List of dependencies for users |
| `requirements_dev.txt` | `root` | List of dependencies for developers |
| `docs` | `root/docs` | Package info, API descriptios and tutorials |
| `tests` | `root/tests`| Intergration and unittests |
| `context.py` | `root/tests` | Facilitate tests without installing the package |
| `Makefile` | `root` | Generic management tasks | [link](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/tree/main/tutorials/makefile) |
***

## What to put in your porject
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
### `requirements.txt` & `requirements_dev.txt`
- It should specify the dependencies required.
- Check this out [how to generate a requirements.txt](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/requirements.md) if you want to know more.
- Generally, it is good practice to keep to file, one for normal usage and one for development where you can you put the requiremetns for testing, building, and generating documentation.
- This file is not requied if (generally people put both options):
    - There are no dependencies.
    - There is a preference to set up the environment via `setup.py`.

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
***

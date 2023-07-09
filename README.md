# Template for your Python project
- This repo is a template with explanation.
- The real tamplate which can be copy is located under the `template` folder.
***

## Module vs. packages
- **module** – a module is a file containing Python functions.
- **package** – a package is a collection of modules intended to be installed and used together.
- This templates focuses on you to build a package.
- [Module vs. Package vs. Library vs. Framework](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/modules_packages_libraries_frameworks.md)
***

## The `Setup.cfg` file
- This file is no longer required for configuring a package, but third-party tools may still use it. 
***

## The `pyproject.toml` file
- This is what replaces `setup.cfg`.
***

## The `test` folder
- The test folder go at the top-level of the project with an `__init__.py` file so they are discoverable by applications like `pytest`.
- The alternative of placing them inside the src/mypackage directory means they will get deployed into production which may not be desirable.
***

## The `src` folder
- It prevents tools like pytest incidently importing it.
***

## `setup.py` file
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
- If you do not intend to publish your project then this file is NOT required at all, and `pip install -e .` will still work. `e` stands for `editable`.
- This will add a symlink into your site-packages folder and make your local project behave as if it was fully installed while at the same time you can continue editing. This saves you from adding this at the to of the file:
```python
import sys
sys.path.append("../")
```
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

## References
- [How to build your first python package](https://towardsdatascience.com/how-to-build-your-first-python-package-6a00b02635c9)
- [Publishing packages and modules](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
- [Understanding setup.py, setup.cfg and pyproject.toml in Python](https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/)
- [Avoiding `sys.path.append(..)` for imports](https://stackoverflow.com/questions/68033795/avoiding-sys-path-append-for-imports)
***

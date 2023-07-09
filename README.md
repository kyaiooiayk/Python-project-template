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

## References
- [How to build your first python package](https://towardsdatascience.com/how-to-build-your-first-python-package-6a00b02635c9)
- [Publishing packages and modules](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
- [Understanding setup.py, setup.cfg and pyproject.toml in Python](https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/)
***

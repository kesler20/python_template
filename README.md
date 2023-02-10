# Python Tempalte

the following files, inlcuding:
- `pyproject.toml`
- `setup.py`

are required for the python application to be installed as a python package. This will allow to import the various modules within the package from any part of the programme and to run tests using `pytest` accordingly.

run pre-commit install

this can be viewed as we used --cov on the configuration file
a 100% test coverage means that all your tests combined cover every single line of executable code


to get the coverage report after running ``pytest tests`` (make sure that you have the ``.coverage``)
to get the coverage report run
coverage html
then to see the report go to the htmlcov folder and launch the index.html

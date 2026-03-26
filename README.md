# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.


# To install and use the published package (easiest for end-users):

Then, in Python code, import and use it (e.g., from snackoracle import predict_snack_vibe).

To develop/modify the code (for team members contributing):

Clone the repo.
Set up the environment: pipenv install (installs dependencies from Pipfile).
Run tests: pipenv run pytest or pipenv run python -m pytest.
Build locally if needed: pipenv run python -m build.
To run the example: pipenv run python example.py.
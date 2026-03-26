# Snack Oracle (Komodo Dragons)

[![log github events](https://github.com/swe-students-spring2026/3-package-komodo_dragon/actions/workflows/event-logger.yml/badge.svg?branch=main)](https://github.com/swe-students-spring2026/3-package-komodo_dragon/actions/workflows/event-logger.yml)

Above badge shows the result of the most recent workflow on the main branch. 

---

## About this project

**Snack Oracle** is a Python package that turns moods, weather, hunger, and late-night energy into snack suggestions and more. It is distributed on PyPI so anyone can install it with `pip` and import it from their own programs.

**PyPI:** [snackoracle](https://pypi.org/project/snackoracle/) · [release 0.1.0](https://pypi.org/project/snackoracle/0.1.0/)

---

## Install and import:

Install from PyPI:

```bash
pip install snackoracle==0.1.0
```

Import the module and call any function. Copy-paste examples for every public function:

```python
from snackoracle import (
    recommend_snack,
    snack_prophecy,
    snack_vibe,
    calorie_denial,
    snack_compatibility,
    midnight_snack_risk,
    snack_aura_reading,
)

print(recommend_snack("happy", 5))
print(snack_prophecy("wednesday", 5))
print(snack_vibe("rainy", "sad"))
print(calorie_denial("chips", 3))
print(snack_compatibility("chips", "dip"))
print(midnight_snack_risk(hours_awake=3, self_control=4))
print(
    snack_aura_reading(
        current_emotion="stressed",
        favorite_flavor="Flamin' Hot Cheetos",
    )
)
```

**Runnable demo:** [`example.py`](./example.py) calls each of the functions above (same idea as the block you can paste into a REPL or script).

---

## Contribute: virtualenv, dependencies, test, and build

These steps work on **Windows, macOS, and Linux** as long as Python 3.10+ is installed.

1. **Clone** repository

2. **Install pipenv:**

   ```bash
   python -m pip install --user pipenv
   ```

3. From the **project root**, create the virtual environment and install dev dependencies (pytest, build):

   ```bash
   pipenv install --dev
   ```

4. **Run tests:**

   ```bash
   pipenv run pytest
   ```

5. **Build**:

   ```bash
   pipenv run python -m build
   ```

6. **Run the example** (uses every function):

   ```bash
   pipenv run python example.py
   ```

---

## Configure, run, environment variables, and data

- **Run:** There is no long-running server. 
- **Environment variables:** None required.
- **Database:** None. No starter data import.
- **Secrets / `.env`:** This project does not use secret configuration files in the repo. 

---

## Team

- [CHEology](https://github.com/CHEology)
- [abirmahmood6](https://github.com/abirmahmood6)
- [rohanmalhotra0](https://github.com/rohanmalhotra0)
- [KarenMazaDelgado](https://github.com/KarenMazaDelgado)


# To install and use the published package (easiest for end-users):

Then, in Python code, import and use it (e.g., from snackoracle import predict_snack_vibe).

To develop/modify the code (for team members contributing):

Clone the repo.
Set up the environment: pipenv install (installs dependencies from Pipfile).
Run tests: pipenv run pytest or pipenv run python -m pytest.
Build locally if needed: pipenv run python -m build.
To run the example: pipenv run python example.py.
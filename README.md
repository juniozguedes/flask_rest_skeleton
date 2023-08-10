# Create venv

```
python -m venv venv
```

# Install requirements

```
pip install -r requirements.txt
```

# Install Pre-commit (Optional)

```
pre-commit install
```

# Run the project

```
waitress-serve --call 'app:create_app'
```

# Pytest

Pytest with logs:

```
 pytest -s -v
```

# Linter checking

To check pre-commit status:

```
 pre-commit run --all-files
```

# Freezing requirements with venv

Might change depending on the OS, but the idea is to freeze requirements starting from the pip inside venv folder:

```
 .\venv\Scripts\pip3 freeze > requirements.txt
```

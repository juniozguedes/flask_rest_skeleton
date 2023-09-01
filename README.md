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
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

# Run the project with Docker

```
docker build --force-rm -t flask-app .
docker run --rm -p 8000:8000 flask-app
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

# Create a local database with PostgreSQL

docker run -p 5432:5432 -v /tmp/database:/var/lib/postgresql/data -e POSTGRES_PASSWORD=1234 -d postgres

# Template for Vite, Tailwind, React Application (Python Flask Backend)

This is a TypeScript/Python template project which contains a Python Flask backend and a Vite, Tailwind, React frontend.

**TODO** Keep this in-line with the other template project. Need a startup procedure.

## Dependencies

Install dependencies with the following commands:

```bash
pip install Flask \
  SQLAlchemy Flask-SQLAlchemy psycopg2-binary \
  marshmallow marshmallow-sqlalchemy flask-marshmallow \
  pytest pytest-flask
```

## Setup

This application requires a configuration file named `config.py` in order to run.
There is an example configuration file named `config.py.example` that you can rename
or copy and customize for your needs.

**TODO** Talk about default config being `development`. It can be controlled with the `PYTHON_ENV` environment variable.

To set up the database, please run the [`initialize_db.py`](./scripts/initialize_db.py) script.

```bash
python3 -m scripts.initialize_db
```

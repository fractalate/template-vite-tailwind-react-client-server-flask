# Template for Vite, Tailwind, React Application (Python Flask Backend)

This is a TypeScript/Python template project which contains a Python Flask backend and a Vite, Tailwind, React frontend.

## Dependencies

Install dependencies with the following commands:

```bash
pip install Flask \
  SQLAlchemy Flask-SQLAlchemy psycopg2-binary \
  marshmallow marshmallow-sqlalchemy flask-marshmallow \
  requests \
  flask-socketio \
  pytest pytest-flask
```

## Setup

This application requires a configuration file named `config.py` in order to run which you will have to create yourself.
There is an example configuration file named `config.py.example` that you can rename
or copy and customize for your needs.

The application can run in several different modes which are controllable with the `PYTHON_ENV`:

* `development` (default) - Run the server in development mode with hot reloading.
* `production` - Run the server in production mode.
* `testing` - Run the server in testing mode. This is the mode that is used during tests, you shouldn't use it directly.

To set up the database, please run the [`initialize_db.py`](./scripts/initialize_db.py) script.

```bash
python3 -m scripts.initialize_db
```

The client requires its dependencies to be installed. To do this, navigate to the [client](client/) directory and run the following commands:

```bash
npm install .
```

## Development

To run the application in development mode, run the provided `dev-client-server.sh` script:

```bash
./dev-client-server.sh
```

## Testing

You can run the included tests with the following commands:

```bash
python3 -m pytest tests
```

Be sure to create the database configured for `testing` in your `config.py` before running the tests.

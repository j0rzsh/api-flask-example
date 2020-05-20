# api-flask-example

Example of an API in Flask with Docker

## Build docker container

```bash
docker build -t example-api[:version] .
```

## Run the app (in Docker)

Just run in the command line

```bash
docker run -d -p 8000:8000 example-api
```

And in your browser look for `localhost:8000`

## Running in dev mode (as a Python app)

Run app.py

```bash
python src/app.py
```

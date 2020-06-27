# api-flask-example

Example of an API in Flask with Docker

## Build docker container

```bash
docker build -t example-api[:version] .
```

## Run the app (using Docker-Compose)

Requirements: docker-compose installed

```bash
docker-compose up
```

## Run the app (using Nomad)

Requirements: docker image uploaded in DockerHub, and Nomad installed.

Start a nomad agent (in this example, in dev mode):

```bash
nomad agent -dev
```

In another shell, run:

```bash
nomad run example.nomad
```

Now Nomad's UI is available in localhost:4646 and the api is available in localhost:8000

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

### Note

werkzeug is fixed to version 0.16.1 because of a bug in version 1.0.0: [flask-restplus is broken by Werkzeug 1.0.0](https://github.com/noirbizarre/flask-restplus/issues/777)

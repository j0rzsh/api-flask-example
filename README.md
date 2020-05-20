# api-flask-example

Example of an API in Flask with Docker

## Build docker container

```bash
docker build -t example-api[:version] .
```

## Run the app (using Nomad)

Requeriments: docker image uploaded in DockerHub, and Nomad installed.

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

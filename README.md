# student-ml-api

A simple ML prediction API built with FastAPI and containerized with Docker.

## Endpoints

- `GET /health` — Health check with application and model metadata
- `POST /predict` — Accepts `{"value": N}` and returns `{"input": N, "prediction": 2*N}`

## Running Locally

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 5000
```

## Running with Docker

```bash
docker build -t student-ml-api:1.0.0 .
docker run -d -p 5000:5000 student-ml-api:1.0.0
```

## Running Tests

```bash
pytest -v
```

## CI/CD

- Pull requests trigger CI (tests + Docker build validation)
- Version tags (`v*.*.*`) trigger the release workflow, which builds and pushes to GHCR

## Registry

```
ghcr.io/salarshoaib/student-ml-api
```

# Random Number API - Kubernetes Project

A simple FastAPI application that returns random numbers from 1 to 10, deployed on Kubernetes.

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check endpoint
- `GET /random` - Returns a random number between 1 and 10

## Project Structure

```
.
├── app.py                 # FastAPI application
├── models/
│   ├── __init__.py
│   └── schemas.py        # Pydantic models
├── Dockerfile            # Container image definition
├── requirements.txt      # Python dependencies
└── kubernetes/
    ├── deployment.yaml   # Kubernetes deployment (3 replicas)
    └── service.yaml      # NodePort service (port 30080)
```

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app:app --reload

# Access at http://localhost:8000
```

## Docker

```bash
# Build image
docker build -t random-api:latest .

# Run container
docker run -p 8000:8000 random-api:latest
```

## Kubernetes Deployment


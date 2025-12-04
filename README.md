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

### Using Minikube

```bash
# Start minikube
minikube start

# Load image into minikube
minikube image load random-api:latest

# Deploy to Kubernetes
kubectl apply -f kubernetes/

# Access the service
minikube service random-api-service

# Check deployment status
kubectl get pods
kubectl get services
```

### Using kind

```bash
# Create cluster
kind create cluster

# Load image into kind
kind load docker-image random-api:latest

# Deploy to Kubernetes
kubectl apply -f kubernetes/

# Port forward to access locally
kubectl port-forward service/random-api-service 8080:80
```

## Testing

```bash
# Test root endpoint
curl http://localhost:8000/

# Test health endpoint
curl http://localhost:8000/health

# Test random number endpoint
curl http://localhost:8000/random
```

## Kubernetes Resources

- **Deployment**: 3 replicas with health checks
- **Service**: NodePort type, accessible on port 30080
- **Resource limits**: 256Mi memory, 500m CPU

from fastapi import FastAPI
import random

from models import HealthResponse, RandomResponse

app = FastAPI(title="Random Number API")


@app.get("/")
async def root():
    return {"message": "Welcome to Random Number API on Kubernetes!"}


@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        message="Application is running"
    )


@app.get("/random", response_model=RandomResponse)
async def get_random_number():
    return RandomResponse(number=random.randint(1, 10))

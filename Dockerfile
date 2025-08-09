FROM ubuntu:latest
LABEL authors="kamal"

ENTRYPOINT ["top", "-b"]

# Use minimal Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system deps if needed (e.g., gcc for xgboost)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better layer caching)
COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose Cloud Run port
EXPOSE 8080

# Run FastAPI app
CMD ["uvicorn", "apps.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "1"]





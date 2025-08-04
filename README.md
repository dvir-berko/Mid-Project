# 🛍️ Flask Orders API

A simple REST API built with Flask to manage travel orders, Dockerized and deployable with Kubernetes.

## Features

- `GET /orders`: Retrieve a list of random travel orders (first-time only)
- `POST /orders`: Add a new order (auto-assigned ID)
- `GET /`: Health check and welcome message

## Quick Start

### 🐳 Build & Push Docker Image


```bash
docker build -t your-dockerhub-username/flask-orders:latest .
docker push your-dockerhub-username/flask-orders:latest

Deploy on Minikube
minikube start --driver=docker
kubectl apply -f k8s/
minikube service flask-orders-service


✅ Test API
chmod +x test-api.sh
./test-api.sh


🧱 Project Structure

.
├── app.py
├── requirements.txt
├── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── test-api.sh


📦 Built With
Python 3.10

Flask 2.2.5

Docker & Docker Hub

Kubernetes (Minikube)


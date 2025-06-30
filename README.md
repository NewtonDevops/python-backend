# 🐍 Python Flask Backend – Docker & Minikube Setup

This is a simple Flask-based backend API used in Kubernetes training environments.  
It returns a JSON greeting when accessed on the root path


---

## 🐳 Step 1: Build the Docker Image Locally

Clone this code by running 
```bash
git clone 
```

Run this from the project root directory:

```bash
docker build -t python-backend .
```

## 🧪 Step 2: Test the Docker Image Locally
Start the container:

```bash
docker run --rm -p 8080:8080 python-backend:latest
```
In another terminal, run:

```bash
curl http://localhost:8080
```
Expected response:

```json
{"message":"Hello from the Python backend!"}
```
Press Ctrl+C to stop the container.

## 🚀 Step 3: Build the Image Inside Minikube (Skip Docker Hub)
If you're using Minikube and want to make the image available directly inside the cluster:

#### Point your Docker CLI to Minikube's Docker engine:
```bash
eval $(minikube docker-env)
```
#### Build the image inside Minikube:
```bash
docker build -t python-backend .
```
✅ You do not need to push the image to Docker Hub. Kubernetes will be able to use it directly.

## 🔄 Step 4: Revert Docker to Your Host (Optional)
To return your terminal to your local machine's Docker context:

```bash
eval $(minikube docker-env -u)
```

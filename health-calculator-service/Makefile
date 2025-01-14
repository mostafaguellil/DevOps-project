# Variables
APP_NAME = health-calculator
IMAGE_NAME = health-calculator:latest
PORT = 4000

# Default target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  all            Run the entire workflow (install, test, build-docker, run-docker)"
	@echo "  install        Install dependencies"
	@echo "  run            Run the Flask application locally"
	@echo "  test           Run unit tests"
	@echo "  build-docker   Build the Docker image"
	@echo "  run-docker     Run the Docker container"
	@echo "  stop-docker    Stop the running Docker container"

# Run the entire workflow
.PHONY: all
all: install test build-docker run-docker

# Install dependencies
.PHONY: install
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Run the Flask app locally
.PHONY: run
run:
	@echo "Running the Flask application..."
	python app.py

# Run tests
.PHONY: test
test:
	@echo "Running unit tests..."
	python -m unittest test.py

# Build the Docker image
.PHONY: build-docker
build-docker:
	@echo "Building the Docker image..."
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
.PHONY: run-docker
run-docker:
	@echo "Running the Docker container..."
	docker run -p $(PORT):5000 --name $(APP_NAME) $(IMAGE_NAME)

# Stop the running Docker container
.PHONY: stop-docker
stop-docker:
	@echo "Stopping the Docker container..."
	docker stop $(APP_NAME) || true
	docker rm $(APP_NAME) || true
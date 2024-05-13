# Automated e2e tests

**Tech Stack**
Python 3.12, pytest, requests, Faker, Docker

## Prerequisites
1. Install Python 3.12 from https://www.python.org/ [optional, only for local machine]
2. Install Docker from https://docs.docker.com/engine/install/

## Solution Explained

This project provides a comprehensive test suite for the JSON Placeholder API posts endpoint. It utilizes the requests library to make HTTP requests and pytest to test different scenarios.

Key Features:

- Functional Tests: Verifies API behavior for various HTTP methods formats (GET, POST, PUT, DELETE) and handles expected responses (success, error) with proper data validation using Pydantic models.
- Error Handling: Ensures the API returns appropriate errors for missing parameters, and invalid requests.
- Parallel Execution: For test parallel execution pytest-xdist is used
- Test Data: Dynamic test data has been used with Faker

# Important Folders
- api_response_models = API response models are kept here
- utils = Utils files for different purposes
- reports = reports of Test results
- tests = Tests for API
- logs = Logs of all API requests and responses

    
## Getting Started

#### Install requirements

```
pip install -r requirements.txt
```

### To run API tests locally

```
pytest
```

#### Run API tests and Load tests in docker

```
docker compose build
```

```
docker compose up
```

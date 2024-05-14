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
- Mock Server: A mock server has been implemented with Flask. The mock server usage is controlled by envrionment variable MOCK_SERVER. If MOCK_SERVER is 1 then mock server is used in the tests.
- Parallel Execution: For test parallel execution pytest-parallel is used. With parallel execution and mock server does not give stable results. It is advised to use parallel execution with the real API. It needs to manually activated by adding ```--workers 2``` argument like this.
- Test Data: Dynamic test data and mock response has been generated with Faker.

# Important Folders
- api_response_models = API response models are kept here
- api_wrappers - API wrappers for different APIs
- clients - Differnt API clients. Currently only HTTP Rest API client is implemented.
- mock_server - Mock flask server
- random_data - Dynamic random for testing and mocking API responses
- utils = Utils methods for different purposes
- reports = Reports of Test results
- tests = Tests for JSON Placeholder API Posts
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

### To run API tests parallaly

```
pytest --workers 2
```

#### Run API tests and Load tests in docker

```
docker compose build
```

```
docker compose up
```

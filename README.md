# Python Requests — API Testing & Automation Guide

## 📌 Overview

The **Requests** library is one of the most popular Python libraries for working with HTTP APIs.

It allows you to send HTTP requests such as:

- `GET`
- `POST`
- `PUT`
- `PATCH`
- `DELETE`
- `HEAD`
- `OPTIONS`

For QA/SDET engineers, `requests` is commonly used for:

- API testing
- REST API automation
- API smoke testing
- API regression testing
- Authentication testing
- Request/response validation
- API chaining
- Test data creation
- Backend validation
- Integration testing

---

# 1. What is Requests?

`requests` is a Python HTTP client library.

It provides a simple way to communicate with web servers and REST APIs.

### Example

```python
import requests

response = requests.get("https://api.github.com/users")

print(response.status_code)
print(response.text)
```

The flow is:

```text
Python Test
     |
     v
requests library
     |
     v
HTTP Request
     |
     v
API Server
     |
     v
HTTP Response
     |
     v
Python Test
```

---

# 2. How to Install Requests

## Step 1 — Verify Python

Open Command Prompt or PowerShell:

```bash
python --version
```

Example:

```text
Python 3.14.7
```

You can also use:

```bash
py --version
```

---

## Step 2 — Install Requests

Run:

```bash
pip install requests
```

Recommended:

```bash
python -m pip install requests
```

If you are using a virtual environment:

```bash
python -m pip install requests
```

---

# 3. Verify Installation

Run:

```bash
pip show requests
```

You should see information similar to:

```text
Name: requests
Version: 2.x.x
Location: ...
```

You can also verify using Python:

```python
import requests

print(requests.__version__)
```

---

# 4. Create a Simple Project

Recommended project structure:

```text
python-api-automation/
│
├── tests/
│   ├── test_get_users.py
│   ├── test_create_user.py
│   └── test_update_user.py
│
├── utils/
│   └── api_client.py
│
├── data/
│   └── test_data.json
│
├── requirements.txt
└── README.md
```

Create `requirements.txt`:

```text
requests
pytest
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 5. Understanding API Requests

An HTTP API request generally contains:

```text
HTTP Request
│
├── Method
├── URL
├── Headers
├── Query Parameters
├── Path Parameters
├── Request Body
└── Authentication
```

Example:

```http
GET https://api.example.com/users
```

The server returns an HTTP response:

```text
HTTP Response
│
├── Status Code
├── Headers
└── Response Body
```

---

# 6. GET Request

The `GET` method is generally used to retrieve data.

```python
import requests

url = "https://api.github.com/users"

response = requests.get(url)

print(response.status_code)
print(response.text)
```

---

# 7. Response Status Code

Always validate the status code in API testing.

```python
assert response.status_code == 200
```

Common status codes:

| Status Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 202 | Accepted |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |

---

# 8. Reading Response Text

```python
print(response.text)
```

`response.text` returns the response as a string.

Example:

```python
response = requests.get("https://api.github.com/users")

print(response.text)
```

---

# 9. Reading JSON Response

Most REST APIs return JSON.

Use:

```python
data = response.json()

print(data)
```

Example:

```python
response = requests.get("https://api.github.com/users")

data = response.json()

print(data[0])
```

---

# 10. Accessing JSON Fields

Suppose the API returns:

```json
{
    "id": 101,
    "name": "John",
    "email": "john@example.com"
}
```

Python:

```python
data = response.json()

print(data["id"])
print(data["name"])
print(data["email"])
```

---

# 11. POST Request

`POST` is generally used to create a resource.

Example:

```python
import requests

url = "https://api.example.com/users"

payload = {
    "name": "John",
    "email": "john@example.com"
}

response = requests.post(
    url,
    json=payload
)

print(response.status_code)
print(response.json())
```

---

# 12. `json=` vs `data=`

For JSON APIs, prefer:

```python
requests.post(
    url,
    json=payload
)
```

rather than:

```python
requests.post(
    url,
    data=payload
)
```

### JSON request

```python
payload = {
    "username": "john",
    "password": "password123"
}

response = requests.post(
    url,
    json=payload
)
```

The `requests` library handles JSON serialization for you.

---

# 13. PUT Request

`PUT` is generally used to update or replace a resource.

```python
import requests

url = "https://api.example.com/users/101"

payload = {
    "name": "John Updated",
    "email": "john.updated@example.com"
}

response = requests.put(
    url,
    json=payload
)

print(response.status_code)
print(response.json())
```

---

# 14. PATCH Request

`PATCH` is generally used for a partial update.

```python
payload = {
    "email": "newemail@example.com"
}

response = requests.patch(
    "https://api.example.com/users/101",
    json=payload
)

print(response.status_code)
```

Difference:

```text
PUT
 |
 +-- Usually replaces the resource

PATCH
 |
 +-- Usually updates selected fields
```

The exact behavior depends on the API contract.

---

# 15. DELETE Request

`DELETE` is used to delete a resource.

```python
import requests

url = "https://api.example.com/users/101"

response = requests.delete(url)

print(response.status_code)
```

A successful DELETE may return:

```text
204 No Content
```

In that case, don't assume there is a JSON response.

---

# 16. Headers

Headers provide additional information about the request.

Example:

```python
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.get(
    url,
    headers=headers
)
```

Common headers:

```text
Content-Type
Accept
Authorization
User-Agent
Cookie
```

---

# 17. Authentication

APIs commonly use authentication.

One common approach is a Bearer token.

```python
token = "your-token"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.get(
    url,
    headers=headers
)
```

The resulting HTTP header is:

```http
Authorization: Bearer your-token
```

### Important

Do not hard-code real tokens in source code.

Avoid:

```python
token = "abc123-real-secret-token"
```

Prefer environment variables or a secrets-management solution.

---

# 18. Basic Authentication

Requests supports Basic Authentication:

```python
import requests

response = requests.get(
    url,
    auth=("username", "password")
)

print(response.status_code)
```

---

# 19. Query Parameters

Query parameters are commonly used to filter or search data.

Example URL:

```text
https://api.example.com/users?page=2&limit=10
```

Instead of manually constructing the URL:

```python
params = {
    "page": 2,
    "limit": 10
}

response = requests.get(
    "https://api.example.com/users",
    params=params
)
```

Requests builds the query string.

---

# 20. Path Parameters

Path parameters are part of the URL.

Example:

```text
/users/101
```

Python:

```python
user_id = 101

url = f"https://api.example.com/users/{user_id}"

response = requests.get(url)
```

---

# 21. Timeout

Always consider setting a timeout for automation code.

```python
response = requests.get(
    url,
    timeout=10
)
```

Without an appropriate timeout, a request can potentially wait for a long time if the server or network does not respond.

---

# 22. Handling Exceptions

Use exception handling for robust API automation.

```python
import requests

try:
    response = requests.get(
        url,
        timeout=10
    )

    print(response.status_code)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

`RequestException` is the base exception for many Requests-related errors.

---

# 23. `raise_for_status()`

Requests provides:

```python
response.raise_for_status()
```

This raises an exception for unsuccessful HTTP status codes.

Example:

```python
response = requests.get(url)

response.raise_for_status()

print(response.json())
```

For example:

```text
200 → no exception
404 → HTTPError
500 → HTTPError
```

---

# 24. API Validation

As a QA/SDET, don't validate only the status code.

Validate:

### Status Code

```python
assert response.status_code == 200
```

### Response Field

```python
data = response.json()

assert data["name"] == "John"
```

### Response Structure

```python
assert "id" in data
assert "name" in data
assert "email" in data
```

### Response Headers

```python
assert "application/json" in response.headers.get(
    "Content-Type", ""
)
```

---

# 25. Complete GET API Test

Example:

```python
import requests

def test_get_users():

    url = "https://api.example.com/users"

    response = requests.get(
        url,
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data is not None
```

---

# 26. Using Requests with Pytest

Install pytest:

```bash
pip install pytest
```

Create:

```text
tests/test_users.py
```

Example:

```python
import requests

def test_get_users():

    response = requests.get(
        "https://api.example.com/users",
        timeout=10
    )

    assert response.status_code == 200
```

Run:

```bash
pytest
```

Verbose mode:

```bash
pytest -v
```

---

# 27. API Request Chaining

API chaining is very important in real-world API automation.

Example:

```text
Login API
    |
    v
Get Token
    |
    v
Create Customer
    |
    v
Get Customer
    |
    v
Update Customer
    |
    v
Delete Customer
```

Example:

```python
login_response = requests.post(
    login_url,
    json={
        "username": "testuser",
        "password": "password"
    }
)

token = login_response.json()["token"]

headers = {
    "Authorization": f"Bearer {token}"
}

customer_response = requests.post(
    customer_url,
    headers=headers,
    json={
        "name": "John"
    }
)

assert customer_response.status_code == 201
```

---

# 28. Sessions

For multiple requests, `requests.Session()` can be useful.

```python
import requests

session = requests.Session()

session.headers.update({
    "Accept": "application/json"
})

response = session.get(url)
```

A session can persist certain settings such as:

- Headers
- Cookies
- Connection pooling
- Authentication configuration

---

# 29. Cookies

You can send cookies:

```python
cookies = {
    "session_id": "12345"
}

response = requests.get(
    url,
    cookies=cookies
)
```

Read response cookies:

```python
print(response.cookies)
```

---

# 30. Inspecting Request and Response

Useful debugging information:

```python
print(response.status_code)
print(response.headers)
print(response.text)
print(response.url)
```

You can also inspect the prepared request:

```python
print(response.request.method)
print(response.request.url)
print(response.request.headers)
print(response.request.body)
```

Be careful when logging headers because they may contain secrets such as authorization tokens.

---

# 31. File Upload

Requests can upload files using `files=`.

```python
files = {
    "file": open("test.txt", "rb")
}

response = requests.post(
    url,
    files=files
)

print(response.status_code)
```

Prefer a context manager so the file is closed:

```python
with open("test.txt", "rb") as file:

    response = requests.post(
        url,
        files={"file": file}
    )
```

---

# 32. Common HTTP Methods

| Method | Typical Purpose |
|---|---|
| GET | Retrieve data |
| POST | Create/process data |
| PUT | Replace/update resource |
| PATCH | Partially update resource |
| DELETE | Delete resource |
| HEAD | Retrieve headers without response body |
| OPTIONS | Discover supported HTTP operations |

The exact semantics depend on the API specification.

---

# 33. Common Requests Functions

```python
requests.get()
requests.post()
requests.put()
requests.patch()
requests.delete()
requests.head()
requests.options()
```

Example:

```python
response = requests.get(url)
```

---

# 34. Important Response Attributes

```python
response.status_code
response.text
response.content
response.json()
response.headers
response.cookies
response.url
response.request
```

Example:

```python
print(response.status_code)
print(response.headers)
print(response.url)
```

---

# 35. API Testing Checklist

For every API test, consider validating:

```text
✓ HTTP Method
✓ URL
✓ Status Code
✓ Response Body
✓ Response Schema
✓ Response Headers
✓ Response Time
✓ Authentication
✓ Authorization
✓ Query Parameters
✓ Path Parameters
✓ Request Headers
✓ Request Body
✓ Error Response
✓ Boundary Values
✓ Negative Scenarios
```

---

# 36. Positive Testing

Example:

```python
def test_valid_user():

    response = requests.get(
        url,
        timeout=10
    )

    assert response.status_code == 200
```

Test valid:

- Username
- Password
- ID
- Request body
- Headers
- Parameters

---

# 37. Negative Testing

Test invalid scenarios.

Examples:

```text
Invalid username
Invalid password
Missing required field
Invalid ID
Invalid token
Expired token
Missing token
Invalid HTTP method
Malformed JSON
Unsupported content type
```

Example:

```python
response = requests.get(
    url,
    headers={
        "Authorization": "Bearer invalid-token"
    },
    timeout=10
)

assert response.status_code == 401
```

---

# 38. Environment Configuration

Real projects usually have multiple environments:

```text
DEV
QA
UAT
STAGE
PROD
```

Don't hard-code URLs throughout your tests.

Instead:

```python
BASE_URL = "https://qa.example.com"
```

Then:

```python
url = f"{BASE_URL}/users"
```

A better approach is to load configuration from environment variables or configuration files.

Example:

```python
import os

BASE_URL = os.getenv(
    "BASE_URL",
    "https://qa.example.com"
)
```

---

# 39. Recommended API Automation Architecture

For a larger SDET framework:

```text
Python API Automation
│
├── tests/
│   ├── test_login.py
│   ├── test_users.py
│   └── test_accounts.py
│
├── clients/
│   └── api_client.py
│
├── config/
│   └── config.py
│
├── data/
│   ├── users.json
│   └── test_data.json
│
├── utils/
│   ├── logger.py
│   └── helpers.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

# 40. Create an API Client

Instead of repeating Requests code everywhere:

```python
import requests


class APIClient:

    def get(self, url, **kwargs):
        return requests.get(
            url,
            timeout=10,
            **kwargs
        )

    def post(self, url, **kwargs):
        return requests.post(
            url,
            timeout=10,
            **kwargs
        )

    def put(self, url, **kwargs):
        return requests.put(
            url,
            timeout=10,
            **kwargs
        )

    def patch(self, url, **kwargs):
        return requests.patch(
            url,
            timeout=10,
            **kwargs
        )

    def delete(self, url, **kwargs):
        return requests.delete(
            url,
            timeout=10,
            **kwargs
        )
```

Test:

```python
client = APIClient()

response = client.get(
    "https://api.example.com/users"
)

assert response.status_code == 200
```

---

# 41. Useful `requests` Concepts for SDETs

The following concepts are particularly important:

### Beginner

```text
requests.get()
requests.post()
requests.put()
requests.patch()
requests.delete()

status_code
text
json()
headers
params
```

### Intermediate

```text
Session
Authentication
Cookies
Timeout
Exception handling
File upload
Request chaining
Environment configuration
```

### Advanced

```text
Reusable API Client
Fixtures
Data-driven testing
Schema validation
Logging
Reporting
Retry strategy
Parallel execution
CI/CD integration
Mocking
Contract testing
Database validation
```

---

# 42. Requests + Pytest Architecture

A typical SDET implementation:

```text
                 ┌──────────────────┐
                 │      Pytest      │
                 └────────┬─────────┘
                          │
                          v
                 ┌──────────────────┐
                 │   Test Classes   │
                 └────────┬─────────┘
                          │
                          v
                 ┌──────────────────┐
                 │    API Client    │
                 └────────┬─────────┘
                          │
                          v
                 ┌──────────────────┐
                 │     Requests     │
                 └────────┬─────────┘
                          │
                          v
                 ┌──────────────────┐
                 │    REST API      │
                 └──────────────────┘
```

---

# 43. Useful Commands

Install:

```bash
pip install requests
```

Upgrade:

```bash
python -m pip install --upgrade requests
```

Check installation:

```bash
pip show requests
```

List installed packages:

```bash
pip list
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

Run pytest:

```bash
pytest
```

Run with details:

```bash
pytest -v
```

---

# 44. Important Notes

## Note 1 — Always Use Timeouts

Prefer:

```python
requests.get(url, timeout=10)
```

instead of:

```python
requests.get(url)
```

---

## Note 2 — Don't Store Secrets in Code

Avoid:

```python
token = "real-secret-token"
```

Use environment variables or a secret-management system.

---

## Note 3 — Validate More Than Status Code

This is not enough:

```python
assert response.status_code == 200
```

Also validate:

```text
Response body
Required fields
Data types
Headers
Business rules
Response schema
```

---

## Note 4 — Don't Assume Every Response Is JSON

This can fail:

```python
response.json()
```

if the server returns non-JSON content.

Check the API contract and response content type before assuming JSON.

---

## Note 5 — Don't Log Sensitive Information

Avoid logging:

```text
Passwords
Bearer tokens
API keys
Session cookies
Personal information
```

---

## Note 6 — Use Sessions for Multiple Related Requests

```python
session = requests.Session()
```

This can make repeated API interactions cleaner and can reuse connections.

---

# 45. Quick Reference

## GET

```python
requests.get(url)
```

## GET + Parameters

```python
requests.get(
    url,
    params={"id": 10}
)
```

## POST + JSON

```python
requests.post(
    url,
    json=payload
)
```

## PUT

```python
requests.put(
    url,
    json=payload
)
```

## PATCH

```python
requests.patch(
    url,
    json=payload
)
```

## DELETE

```python
requests.delete(url)
```

## Headers

```python
requests.get(
    url,
    headers=headers
)
```

## Authentication

```python
requests.get(
    url,
    auth=(username, password)
)
```

## Timeout

```python
requests.get(
    url,
    timeout=10
)
```

## JSON Response

```python
data = response.json()
```

## Status Code

```python
response.status_code
```

## Raise HTTP Errors

```python
response.raise_for_status()
```

---

# 46. Recommended Learning Path for a QA/SDET

Learn Requests in this order:

```text
1. HTTP Basics
       ↓
2. GET Requests
       ↓
3. POST Requests
       ↓
4. PUT / PATCH
       ↓
5. DELETE
       ↓
6. Status Codes
       ↓
7. Headers
       ↓
8. Query Parameters
       ↓
9. Path Parameters
       ↓
10. JSON
       ↓
11. Authentication
       ↓
12. Cookies
       ↓
13. Sessions
       ↓
14. Exception Handling
       ↓
15. Timeouts
       ↓
16. API Chaining
       ↓
17. Pytest
       ↓
18. API Automation Framework
       ↓
19. Reporting
       ↓
20. CI/CD
```

---

# 47. Final SDET Perspective

`requests` is the **HTTP communication layer**.

Pytest is the **test execution layer**.

A mature API automation framework can be designed as:

```text
                 API Automation Framework
                          │
             ┌────────────┴────────────┐
             │                         │
          Pytest                    Test Data
             │
             v
        API Test Cases
             │
             v
         API Client
             │
             v
         Requests
             │
             v
        HTTP / REST
             │
             v
          API Server
             │
       ┌─────┴─────┐
       │           │
    Database     External
                 Services
```

The key idea is:

> **Requests handles HTTP communication; your test framework handles test logic, assertions, data, reporting, and execution.**

This separation is useful when building a scalable **Python API automation framework for SDET/QE projects**.

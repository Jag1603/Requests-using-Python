# HOW TO MAKE A POST REQUEST
import requests as r
import json

# Basic POST Request
url = "https://reqres.in/api/users"

# Method 1: Using json parameter (automatically sets Content-Type: application/json)
payload = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'job': 'QA Engineer'
}

resp = r.post(url, json=payload)

print("Status Code:", resp.status_code)
print("Response Text:", resp.text)
print("Response JSON:", resp.json())

# Method 2: Using data parameter with manual JSON serialization
payload_json = json.dumps(payload)
headers = {'Content-Type': 'application/json'}

resp2 = r.post(url, data=payload_json, headers=headers)
print("\nAlternative Method:")
print("Status Code:", resp2.status_code)
print("Response:", resp2.json())

# Method 3: POST with Custom Headers
custom_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123'
}

resp3 = r.post(url, json=payload, headers=custom_headers)
print("\nWith Custom Headers:")
print("Status Code:", resp3.status_code)
print("Response:", resp3.json())

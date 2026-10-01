# HOW TO MAKE A PUT REQUEST
import requests as r

# PUT Request - Used to update entire resource
url = "https://reqres.in/api/users/2"

payload = {
    'name': 'Jane Smith',
    'email': 'jane@example.com',
    'job': 'Senior QA Engineer'
}

# Basic PUT Request
resp = r.put(url, json=payload)

print("Status Code:", resp.status_code)
print("Response Text:", resp.text)
print("Response JSON:", resp.json())

# PUT with Custom Headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123'
}

resp2 = r.put(url, json=payload, headers=headers)
print("\nWith Custom Headers:")
print("Status Code:", resp2.status_code)
print("Response:", resp2.json())

# PUT with URL Parameters
params = {'type': 'admin'}
resp3 = r.put(url, json=payload, params=params)
print("\nWith URL Parameters:")
print("URL:", resp3.url)
print("Status Code:", resp3.status_code)

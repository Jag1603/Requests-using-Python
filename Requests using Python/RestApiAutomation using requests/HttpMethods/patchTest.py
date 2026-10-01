# HOW TO MAKE A PATCH REQUEST
import requests as r

# PATCH Request - Used to update partial resource
url = "https://reqres.in/api/users/2"

# PATCH only updates specific fields
payload = {
    'job': 'Lead QA Engineer'
}

# Basic PATCH Request
resp = r.patch(url, json=payload)

print("Status Code:", resp.status_code)
print("Response Text:", resp.text)
print("Response JSON:", resp.json())

# PATCH with multiple fields
payload2 = {
    'name': 'Alice Johnson',
    'job': 'Test Lead'
}

resp2 = r.patch(url, json=payload2)
print("\nPATCH Multiple Fields:")
print("Status Code:", resp2.status_code)
print("Response:", resp2.json())

# PATCH with Custom Headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123'
}

resp3 = r.patch(url, json=payload, headers=headers)
print("\nWith Custom Headers:")
print("Status Code:", resp3.status_code)
print("Response:", resp3.json())

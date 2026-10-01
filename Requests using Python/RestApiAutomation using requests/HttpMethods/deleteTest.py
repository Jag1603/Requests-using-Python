# HOW TO MAKE A DELETE REQUEST
import requests as r

# DELETE Request - Used to delete a resource
url = "https://reqres.in/api/users/2"

# Basic DELETE Request
resp = r.delete(url)

print("Status Code:", resp.status_code)
print("Response Text:", resp.text)
print("Response Length:", len(resp.text))

# DELETE with Custom Headers
headers = {
    'Authorization': 'Bearer token123'
}

resp2 = r.delete(url, headers=headers)
print("\nWith Custom Headers:")
print("Status Code:", resp2.status_code)
print("Response:", resp2.text)

# DELETE with URL Parameters
params = {'force': 'true'}
resp3 = r.delete(url, params=params, headers=headers)
print("\nWith URL Parameters:")
print("URL:", resp3.url)
print("Status Code:", resp3.status_code)

# DELETE with Body (Some APIs require this)
payload = {'reason': 'User inactive'}
resp4 = r.delete(url, json=payload, headers=headers)
print("\nWith Body:")
print("Status Code:", resp4.status_code)
print("Response:", resp4.text)

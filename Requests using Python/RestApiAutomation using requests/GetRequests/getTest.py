# HOW TO MAKE A REQUEST
import requests as r
resp= r.get("https://reqres.in/api/users/2")
# How to Get Status Code
print("status code is : ", resp.status_code)
# How to Print status
print(resp.text)
# How to get Response encoding
print(resp.encoding)
# How to Deal with Content Type
print(resp.headers['content-type'])
# How to get Response Json Details
print(resp.json)


print(type(resp))
# How to Get Raw Response content

print(resp.raw)

# Note that any dictionary key whose value is None will not be added to the URL’s query string.
# HOW TO PASS Parameters in Url

payload = {'key1': 'value1', 'key2': 'value2'}

resp_payload= r.get('https://reqres.in/api/users/2',payload)
print(resp_payload.url)


# How to Create  Custom Headers

headers = {'Application': 'server/0.0.0.1'}
resp_custom_header= r.get("https://reqres.in/api/users/2",headers=headers)

print(resp_custom_header.headers)







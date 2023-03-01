

import requests as r
resp= r.get("https://www.google.com/")
# How to Get Status Code
print("status code is : ", resp.status_code)
print(resp.cookies)

# How to create a Custom Cookie

Cookies= dict(samplecookie=" my cookie")
cookie_url= r.get("https://www.google.com/",Cookies)
print(cookie_url.cookies)

# If you’re using GET, OPTIONS, POST, PUT, PATCH or DELETE, you can disable redirection handling with the
# allow_redirects parameter:
s = r.get('http://github.com/', allow_redirects=False)
print(s)


# If you’re using HEAD, you can enable redirection as well:

k = r.head('http://github.com/', allow_redirects=True)


# COMPLETE EXAMPLE - ALL HTTP METHODS (GET, POST, PUT, PATCH, DELETE)
import requests as r
import json

BASE_URL = "https://reqres.in/api/users"

# ============ GET REQUEST ============
print("\n=== GET REQUEST ===")
get_url = f"{BASE_URL}/2"
get_resp = r.get(get_url)
print(f"GET {get_url}")
print(f"Status Code: {get_resp.status_code}")
print(f"Response: {json.dumps(get_resp.json(), indent=2)}")

# ============ POST REQUEST ============
print("\n=== POST REQUEST ===")
post_payload = {
    'name': 'John Doe',
    'job': 'Software Engineer'
}
post_resp = r.post(BASE_URL, json=post_payload)
print(f"POST {BASE_URL}")
print(f"Payload: {post_payload}")
print(f"Status Code: {post_resp.status_code}")
print(f"Response: {json.dumps(post_resp.json(), indent=2)}")

# ============ PUT REQUEST ============
print("\n=== PUT REQUEST ===")
put_url = f"{BASE_URL}/2"
put_payload = {
    'name': 'Jane Smith',
    'job': 'QA Engineer'
}
put_resp = r.put(put_url, json=put_payload)
print(f"PUT {put_url}")
print(f"Payload: {put_payload}")
print(f"Status Code: {put_resp.status_code}")
print(f"Response: {json.dumps(put_resp.json(), indent=2)}")

# ============ PATCH REQUEST ============
print("\n=== PATCH REQUEST ===")
patch_url = f"{BASE_URL}/2"
patch_payload = {
    'job': 'Test Lead'
}
patch_resp = r.patch(patch_url, json=patch_payload)
print(f"PATCH {patch_url}")
print(f"Payload: {patch_payload}")
print(f"Status Code: {patch_resp.status_code}")
print(f"Response: {json.dumps(patch_resp.json(), indent=2)}")

# ============ DELETE REQUEST ============
print("\n=== DELETE REQUEST ===")
delete_url = f"{BASE_URL}/2"
delete_resp = r.delete(delete_url)
print(f"DELETE {delete_url}")
print(f"Status Code: {delete_resp.status_code}")
print(f"Response: {delete_resp.text}")

# ============ SUMMARY ============
print("\n=== SUMMARY ===")
print(f"GET Status: {get_resp.status_code}")
print(f"POST Status: {post_resp.status_code}")
print(f"PUT Status: {put_resp.status_code}")
print(f"PATCH Status: {patch_resp.status_code}")
print(f"DELETE Status: {delete_resp.status_code}")

"""
Comprehensive Examples of HTTP Methods using Requests Library in Python

This module demonstrates how to use the requests library for API automation
with examples for GET, POST, PUT, DELETE, PATCH, and other HTTP methods.

Installation:
    pip install requests
"""

import requests
import json
from typing import Dict, Any, Optional

# Base URL for examples (using JSONPlaceholder - a free REST API for testing)
BASE_URL = "https://jsonplaceholder.typicode.com"


# ============================================================================
# 1. GET REQUEST EXAMPLES
# ============================================================================

def simple_get_request():
    """
    Simple GET request to fetch data from an API endpoint.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- Simple GET Request ---")
    url = f"{BASE_URL}/posts/1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def get_with_parameters():
    """
    GET request with query parameters.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- GET Request with Parameters ---")
    url = f"{BASE_URL}/posts"
    
    # Method 1: Using params dictionary
    params = {
        'userId': 1,
        '_limit': 5,  # Limit results to 5
        '_sort': 'id',
        '_order': 'desc'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print(f"Number of posts: {len(response.json())}")
        print(f"First post: {response.json()[0]}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def get_with_headers():
    """
    GET request with custom headers.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- GET Request with Custom Headers ---")
    url = f"{BASE_URL}/posts/1"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'application/json',
        'Authorization': 'Bearer your_token_here'  # For APIs requiring authentication
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('content-type')}")
        print(f"Response: {response.json()}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def get_with_timeout():
    """
    GET request with timeout to prevent hanging.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- GET Request with Timeout ---")
    url = f"{BASE_URL}/posts/1"
    
    try:
        # Timeout in seconds (connect timeout, read timeout)
        response = requests.get(url, timeout=(5, 10))
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print("Request completed successfully")
        return response
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# ============================================================================
# 2. POST REQUEST EXAMPLES
# ============================================================================

def simple_post_request():
    """
    Simple POST request to create a new resource.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- Simple POST Request ---")
    url = f"{BASE_URL}/posts"
    
    data = {
        'title': 'My First Post',
        'body': 'This is the content of my first post',
        'userId': 1
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print(f"Created Resource: {response.json()}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def post_with_headers_and_auth():
    """
    POST request with custom headers and authentication.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- POST Request with Headers and Auth ---")
    url = f"{BASE_URL}/posts"
    
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Python-Requests-Bot'
    }
    
    data = {
        'title': 'Authenticated Post',
        'body': 'This post requires authentication',
        'userId': 2
    }
    
    try:
        # Basic Authentication
        response = requests.post(
            url,
            json=data,
            headers=headers,
            auth=('username', 'password')
        )
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def post_form_data():
    """
    POST request with form data (not JSON).
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- POST Request with Form Data ---")
    url = f"{BASE_URL}/posts"
    
    # Use 'data' parameter instead of 'json' for form-encoded data
    data = {
        'title': 'Form Data Post',
        'body': 'Posted as form data',
        'userId': 1
    }
    
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def post_file_upload():
    """
    POST request with file upload.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- POST Request with File Upload ---")
    url = f"{BASE_URL}/posts"
    
    try:
        # Uploading a file
        with open('sample.txt', 'rb') as f:
            files = {'file': f}
            response = requests.post(url, files=files)
            response.raise_for_status()
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
            return response
    except FileNotFoundError:
        print("Error: File not found. Create a sample.txt file first.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# ============================================================================
# 3. PUT REQUEST EXAMPLES
# ============================================================================

def simple_put_request():
    """
    Simple PUT request to update an entire resource.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- Simple PUT Request ---")
    url = f"{BASE_URL}/posts/1"
    
    data = {
        'id': 1,
        'title': 'Updated Title',
        'body': 'This is the updated content',
        'userId': 1
    }
    
    try:
        response = requests.put(url, json=data)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print(f"Updated Resource: {response.json()}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def put_with_conditional_headers():
    """
    PUT request with conditional headers (e.g., If-Match for optimistic concurrency).
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- PUT Request with Conditional Headers ---")
    url = f"{BASE_URL}/posts/1"
    
    headers = {
        'If-Match': '"12345"',  # ETag value for optimistic concurrency
        'Content-Type': 'application/json'
    }
    
    data = {
        'id': 1,
        'title': 'Conditionally Updated',
        'body': 'Updated with conditional header',
        'userId': 1
    }
    
    try:
        response = requests.put(url, json=data, headers=headers)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# ============================================================================
# 4. PATCH REQUEST EXAMPLES
# ============================================================================

def simple_patch_request():
    """
    Simple PATCH request to partially update a resource.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- Simple PATCH Request ---")
    url = f"{BASE_URL}/posts/1"
    
    # Only updating specific fields
    data = {
        'title': 'Partially Updated Title'
    }
    
    try:
        response = requests.patch(url, json=data)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print(f"Updated Resource: {response.json()}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# ============================================================================
# 5. DELETE REQUEST EXAMPLES
# ============================================================================

def simple_delete_request():
    """
    Simple DELETE request to remove a resource.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- Simple DELETE Request ---")
    url = f"{BASE_URL}/posts/1"
    
    try:
        response = requests.delete(url)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print("Resource deleted successfully")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def delete_with_verification():
    """
    DELETE request with verification that the resource was deleted.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- DELETE Request with Verification ---")
    url = f"{BASE_URL}/posts/1"
    
    try:
        # Delete the resource
        delete_response = requests.delete(url)
        delete_response.raise_for_status()
        print(f"Delete Status Code: {delete_response.status_code}")
        
        # Verify deletion by attempting to fetch it
        get_response = requests.get(url)
        if get_response.status_code == 404:
            print("Verification: Resource successfully deleted (404 Not Found)")
        else:
            print(f"Verification: Resource still exists (Status: {get_response.status_code})")
        
        return delete_response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# ============================================================================
# 6. OTHER HTTP METHODS
# ============================================================================

def head_request():
    """
    HEAD request to get headers without downloading the body.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- HEAD Request ---")
    url = f"{BASE_URL}/posts/1"
    
    try:
        response = requests.head(url)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print("(No response body for HEAD requests)")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def options_request():
    """
    OPTIONS request to discover what HTTP methods are allowed.
    
    Returns:
        Response object or None if request failed
    """
    print("\n--- OPTIONS Request ---")
    url = f"{BASE_URL}/posts"
    
    try:
        response = requests.options(url)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print(f"Allowed Methods: {response.headers.get('allow', 'Not specified')}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# ============================================================================
# 7. ADVANCED EXAMPLES
# ============================================================================

def session_example():
    """
    Using Session objects for multiple requests with shared settings.
    
    Returns:
        None
    """
    print("\n--- Using Session Object ---")
    
    # Create a session object
    session = requests.Session()
    
    # Set default headers
    session.headers.update({
        'User-Agent': 'My-App/1.0',
        'Accept': 'application/json'
    })
    
    try:
        # All requests made with this session will use the default headers
        response1 = session.get(f"{BASE_URL}/posts/1")
        response2 = session.get(f"{BASE_URL}/posts/2")
        
        print(f"Request 1 Status: {response1.status_code}")
        print(f"Request 2 Status: {response2.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    finally:
        session.close()


def error_handling_example():
    """
    Comprehensive error handling for different types of errors.
    
    Returns:
        None
    """
    print("\n--- Comprehensive Error Handling ---")
    
    url = f"{BASE_URL}/posts/invalid"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise exception for bad status codes
        print(f"Success: {response.json()}")
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Status Code: {e.response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Connection Error: Failed to connect to the server")
    except requests.exceptions.Timeout:
        print("Timeout Error: Request took too long")
    except requests.exceptions.RequestException as e:
        print(f"General Error: {e}")


def json_parsing_example():
    """
    Different ways to handle JSON responses.
    
    Returns:
        None
    """
    print("\n--- JSON Parsing Examples ---")
    
    url = f"{BASE_URL}/posts/1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Method 1: Using .json() method
        data = response.json()
        print(f"Method 1 - .json(): {data}")
        
        # Method 2: Using json.loads() on text
        data = json.loads(response.text)
        print(f"Method 2 - json.loads(): {type(data)}")
        
        # Method 3: Check content type before parsing
        if 'application/json' in response.headers.get('content-type', ''):
            data = response.json()
            print("Method 3 - Content-Type check: JSON response confirmed")
        
        # Access specific fields
        print(f"Post ID: {data['id']}")
        print(f"Post Title: {data['title']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def retry_example():
    """
    Example of retrying a request with exponential backoff.
    
    Returns:
        Response object or None if all retries failed
    """
    print("\n--- Retry with Exponential Backoff ---")
    
    import time
    
    url = f"{BASE_URL}/posts/1"
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            print(f"Success on attempt {attempt + 1}")
            return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
    
    print("All retries exhausted")
    return None


def streaming_response_example():
    """
    Streaming large responses to avoid loading entire content into memory.
    
    Returns:
        None
    """
    print("\n--- Streaming Response ---")
    
    url = f"{BASE_URL}/posts"
    
    try:
        # stream=True prevents downloading the entire response at once
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Read response in chunks
        print(f"Status Code: {response.status_code}")
        print("Reading response in chunks:")
        
        chunk_count = 0
        for chunk in response.iter_content(chunk_size=100):
            if chunk:
                chunk_count += 1
        
        print(f"Total chunks received: {chunk_count}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


# ============================================================================
# 8. COMPLETE WORKFLOW EXAMPLE
# ============================================================================

def complete_workflow_example():
    """
    Complete workflow example: Create, Read, Update, Delete (CRUD).
    
    Returns:
        None
    """
    print("\n" + "="*60)
    print("COMPLETE CRUD WORKFLOW EXAMPLE")
    print("="*60)
    
    base_url = f"{BASE_URL}/posts"
    
    try:
        # CREATE
        print("\n1. CREATE - Posting new resource")
        create_data = {
            'title': 'New Post',
            'body': 'This is a new post',
            'userId': 1
        }
        create_response = requests.post(base_url, json=create_data)
        create_response.raise_for_status()
        created_post = create_response.json()
        post_id = created_post.get('id', 1)
        print(f"Created post ID: {post_id}")
        print(f"Status: {create_response.status_code}")
        
        # READ
        print(f"\n2. READ - Fetching post {post_id}")
        read_response = requests.get(f"{base_url}/{post_id}")
        read_response.raise_for_status()
        print(f"Retrieved: {read_response.json()}")
        print(f"Status: {read_response.status_code}")
        
        # UPDATE
        print(f"\n3. UPDATE - Updating post {post_id}")
        update_data = {
            'id': post_id,
            'title': 'Updated Post Title',
            'body': 'This is the updated content',
            'userId': 1
        }
        update_response = requests.put(f"{base_url}/{post_id}", json=update_data)
        update_response.raise_for_status()
        print(f"Updated: {update_response.json()}")
        print(f"Status: {update_response.status_code}")
        
        # DELETE
        print(f"\n4. DELETE - Deleting post {post_id}")
        delete_response = requests.delete(f"{base_url}/{post_id}")
        delete_response.raise_for_status()
        print(f"Status: {delete_response.status_code}")
        print("Post deleted successfully")
        
    except requests.exceptions.RequestException as e:
        print(f"Error in workflow: {e}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("REQUESTS LIBRARY EXAMPLES")
    print("=" * 60)
    
    # GET Examples
    print("\n" + "="*60)
    print("GET REQUEST EXAMPLES")
    print("="*60)
    simple_get_request()
    get_with_parameters()
    get_with_headers()
    get_with_timeout()
    
    # POST Examples
    print("\n" + "="*60)
    print("POST REQUEST EXAMPLES")
    print("="*60)
    simple_post_request()
    post_with_headers_and_auth()
    post_form_data()
    
    # PUT Examples
    print("\n" + "="*60)
    print("PUT REQUEST EXAMPLES")
    print("="*60)
    simple_put_request()
    put_with_conditional_headers()
    
    # PATCH Examples
    print("\n" + "="*60)
    print("PATCH REQUEST EXAMPLES")
    print("="*60)
    simple_patch_request()
    
    # DELETE Examples
    print("\n" + "="*60)
    print("DELETE REQUEST EXAMPLES")
    print("="*60)
    simple_delete_request()
    
    # Other Methods
    print("\n" + "="*60)
    print("OTHER HTTP METHODS")
    print("="*60)
    head_request()
    options_request()
    
    # Advanced Examples
    print("\n" + "="*60)
    print("ADVANCED EXAMPLES")
    print("="*60)
    session_example()
    error_handling_example()
    json_parsing_example()
    retry_example()
    streaming_response_example()
    
    # Complete Workflow
    complete_workflow_example()
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("="*60)

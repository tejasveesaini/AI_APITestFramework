# Constants
API_URL = "https://jsonplaceholder.typicode.com"
ENDPOINT = "/posts"
METHOD = "POST"
REQUEST_PAYLOAD = {
    "title": 'Post Title',
    "body": 'This post has following body.',
    "userId": 1,
}
EXPECTED_RESPONSE = {
    "id": 101,
    "title": 'Post Title',
    "body": 'This post has following body.',
    "userId": 1
}
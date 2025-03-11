
import sys
import os

from constants import API_URL, ENDPOINT, EXPECTED_RESPONSE, REQUEST_PAYLOAD

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from baseFw.fw_commonMethod import BaseAPITest

class TestPostsAPI(BaseAPITest):
    def __init__(self, base_url):
        super().__init__(base_url)

    def test_create_post(self):
        # Send POST request to create a post
        response = self.send_request("POST", ENDPOINT, REQUEST_PAYLOAD)

        # Verify status code
        self.verify_status_code(response, 201)

        # Parse response JSON
        response_json = response.json()

        # Verify response attributes
        self.verify_response_attributes(response_json, EXPECTED_RESPONSE)

        # Verify dynamic fields
        self.verify_dynamic_fields(response_json, ["id"])

        print("Post creation test passed successfully!")

# Run the test
if __name__ == "__main__":
    # Create an instance of TestPostsAPI
    test_posts_api = TestPostsAPI(API_URL)

    # Run the test
    test_posts_api.test_create_post()
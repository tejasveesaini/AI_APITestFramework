# Specific class for testing the Objects API
from fw_commonMethod import BaseAPITest
from fw_constants import API_URL, ENDPOINT, EXPECTED_RESPONSE, REQUEST_PAYLOAD

class TestObjectAPI(BaseAPITest):
    def __init__(self, base_url):
        super().__init__(base_url)

    def test_create_object(self):
        # Send POST request to create an object
        response = self.send_request("POST", ENDPOINT, REQUEST_PAYLOAD)

        # Verify status code
        self.verify_status_code(response, 200)

        # Parse response JSON
        response_json = response.json()

        # Verify response attributes
        self.verify_response_attributes(response_json, EXPECTED_RESPONSE)

        # Verify dynamic fields
        self.verify_dynamic_fields(response_json, ["id", "createdAt"])

        print("Object creation test passed successfully!")

# Run the test
if __name__ == "__main__":
    # Create an instance of TestObjectAPI
    test_object_api = TestObjectAPI(API_URL)

    # Run the test
    test_object_api.test_create_object()
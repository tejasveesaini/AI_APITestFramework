import requests
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('http_logger')

# Base class for common API testing functionality
class BaseAPITest:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, method, endpoint, payload=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, json=payload)
        logger.info(f"Sending {method} request to {url}")
        logger.info(f"Request payload: {payload}")
        logger.info(f"Response: {response.text}")
        return response

    def verify_status_code(self, response, expected_code):
        logger.info(f"Response status code:  {response.status_code}")
        assert response.status_code == expected_code,f"Expected status code {expected_code}, but got {response.status_code}"

    def verify_response_attributes(self, response_json, expected_attributes):
        
        for key, value in expected_attributes.items():
            if isinstance(value, dict):
                self.verify_response_attributes(response_json[key], value)
            else:
                logger.info(f"Verifying {key} to be {value}")
                assert response_json[key] == value, f"Expected {key} to be {value}, but got {response_json[key]}"

    def verify_dynamic_fields(self, response_json, fields):
        for field in fields:
            logger.info(f"Verifying response contain '{field}' field")
            assert field in response_json, f"Response does not contain '{field}' field"
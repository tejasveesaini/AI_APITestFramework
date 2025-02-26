import requests

# Ollama local server API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Read the file contents
with open("exampleRequestresponse.txt", "r") as file:
    file_content = file.read()
prompt1="Write code in Java for testing the API. Use RestAssured library for making the API request. There should be POJO for request and response."
prompt2="Verify the response attribute values and status code value. Make the code re-usable."
prompt3="The target URL, Request and Response details are as follows:"+file_content
final_prompt = prompt1+prompt2+prompt3
# Define model and prompt
payload = {
    "model": "qwen2.5-coder",  # Change model name if needed
    "prompt": final_prompt,  # Change prompt if needed
    "stream": False,  # Set to True for streaming responses
    "options": {
    "temperature": 0
  },
}

# Make API request
response = requests.post(OLLAMA_API_URL, json=payload)

# Print response
if response.status_code == 200:
    result = response.json()
    print(result["response"])
else:
    print(f"Error: {response.status_code}, {response.text}")

import requests

# Ollama local server API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Read the file contents
with open("payloads/mainPayload.txt", "r") as file:
    file_content = file.read()
with open("baseFw/fw_commonMethod.py", "r") as file:
    fw_commonMethod = file.read()
with open("baseFw/fw_constants.py", "r") as file:
    fw_constants = file.read()
with open("baseFw/fw_testObjectsAPI.py", "r") as file:
    fw_testObjectsAPI = file.read()
prompt1="Write code in Python for testing the API. Use the example provided:\n"
prompt2="CommonMethods Python File:"+fw_commonMethod+" \n Constants Python File:"+fw_constants+"\n Test Script Python File:"+fw_testObjectsAPI+"\n End of Example."
prompt3="The target URL, Request and Response details are as follows:"+file_content
rule1="\n Follow these rules: Do not provide code explanation. \n"
rule2="Do not generate the code for CommonMethods or BaseAPITest but call existing methods."
rule3="Define different constants names than declared in the Constants Python File."
rule4="Identify the dynamic fields and verify the correct data type."
rules=rule1+rule2+rule3+rule4

final_prompt = prompt1+prompt2+prompt3+rules
# Define model and prompt
payload = {
    # "model": "qwen2.5-coder:1.5b",  # Change model name if needed
    "model": "qwen2.5-coder:latest",  # Change model name if needed
    "prompt": final_prompt,  # Change prompt if needed
    "stream": False,  # Set to True for streaming responses
    "options": {
    "temperature": 0,
  },
}

# Make API request to AI model from Ollama API
response = requests.post(OLLAMA_API_URL, json=payload)

# Print response
if response.status_code == 200:
    result = response.json()
    print("Response from AI:")
    print(result["response"])
else:
    print("Error generating code from AI:")
    print(f"Error: {response.status_code}, {response.text}")

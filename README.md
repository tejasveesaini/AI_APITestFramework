# AI_APITestFramework
AI LLM powered framework for API testing. This is currently in "Minimum Viable Product" state. It creates test automation scripts for API testing.

## Overview

This project leverages Ollama's local AI server to automatically generate Python code for API testing. It takes an example request/response file and uses an AI model to create reusable test code that verifies API responses and status codes.

- Files under "baseFw" contains template for code generation. It can be used as a **"standalone API testing framework"** as well.
- mainScript.py contains code for connecting to local AI model and generate the tests

## Screenshots
- Generated code from AI model
<img width="600" alt="image" src="https://github.com/user-attachments/assets/3195a46b-c0ec-4c12-b209-74f88afc33a8" />

- Prompts and Script
<img width="600" alt="image" src="https://github.com/user-attachments/assets/5230c67d-4442-49d8-a667-0e61eaa8d318" />

## Improvement Items
- Segregate payloads into json files and pojo
- Add code to create file with the generated code
- Use bigger model for better responses. For example - detect the dynamic fields

## Requirements

- Python 3.6+
- `requests` library
- Ollama running on localhost (port 11434)
- Qwen2.5-Coder model installed in Ollama

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Ensure Ollama is installed and running on `localhost:11434`
4. Make sure the Qwen2.5-Coder model is installed:
   ```bash
   ollama pull qwen2.5-coder
   ```

## Usage

1. Create a file with your sample API request and response details
2. Run the script:
   ```bash
   python api_test_runner.py
   ```

## How It Works

1. The script reads the example request/response from a text file
2. It constructs a prompt asking for test code generation
3. The prompt is sent to the Ollama API with the Qwen2.5-Coder model
4. The model generates reusable test code based on the provided example
5. The generated code is displayed in the console

## Configuration

You can modify these parameters in the script:
- `OLLAMA_API_URL`: The URL for your Ollama API server
- `file_content`: The path to your example request/response file
- `model`: The Ollama model to use (default: "qwen2.5-coder")
- `temperature`: Controls the randomness of the output (0 = deterministic)

## Example

If your `exampleRequestresponse.txt` contains API details like:

```
URL: https://api.example.com/users
Request Method: POST
Request Headers: {"Content-Type": "application/json"}
Request Body: {"name": "John Doe", "email": "john@example.com"}
Expected Response: {"id": 123, "status": "created"}
Expected Status Code: 201
```

The script will generate test code to verify those specific response values.

## License

[MIT License](LICENSE)

import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# Print expected environment variables and their actual values
print("Expected Environment Variables and Current Values:")
print("=" * 60)

endpoint_env = os.environ.get('AZURE_OPENAI_ENDPOINT', 'NOT SET')
# Use the endpoint exactly as provided by the user (support either with or without '/openai' path)
if endpoint_env != 'NOT SET':
    endpoint = endpoint_env.rstrip('/')
else:
    endpoint = 'NOT SET'

deployment_name = os.environ.get('AZURE_OPENAI_DEPLOYMENT', 'NOT SET')
api_key = os.environ.get('AZURE_OPENAI_API_KEY', 'NOT SET')
api_version = os.environ.get('AZURE_OPENAI_API_VERSION', os.environ.get('OPENAI_API_VERSION', '2024-02-01'))

print(f"AZURE_OPENAI_ENDPOINT: {endpoint}")
print(f"AZURE_OPENAI_DEPLOYMENT: {deployment_name}")
print(f"AZURE_OPENAI_API_KEY: {'***' + api_key[-4:] if api_key != 'NOT SET' and len(api_key) > 4 else api_key}")
print(f"API_VERSION: {api_version}")
print("=" * 60)
print()

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

prompt = "Oh say can you see"
completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
)
print(f"Prompt: {prompt}")
print(f"Response: {completion.choices[0].message.content}")

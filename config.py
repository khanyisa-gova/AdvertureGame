import os
from dotenv import load_dotenv

load_dotenv()
azure_openai_endpoint = os.getenv("azure_endpoint")
azure_openai_api_key = os.getenv("openai_api_key")
azure_deployment = os.getenv("deployment_name")
api_version = os.getenv("openai_api_version")

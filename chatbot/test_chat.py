from langchain.chat_models import ChatOpenAI
from config import OPENAI_API_KEY

llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

response = llm.predict("Give me a hint for exploring a dark forest.")
print("LLM Response:", response)

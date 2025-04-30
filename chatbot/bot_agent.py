from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from config import azure_openai_api_key

llm = ChatOpenAI(temperature=0, openai_api_key=azure_openai_api_key)

def game_hint(input: str) -> str:
    return "You're near a hidden cave. Try using your torch."

tools = [
    Tool(name="game_hint", func=game_hint, description="Provides tips based on game context.")
]

agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")

def get_bot_response(user_input: str) -> str:
    return agent.run(user_input)

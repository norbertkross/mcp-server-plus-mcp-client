import asyncio
import logfire
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerSSE

logfire.configure()
logfire.instrument_pydantic_ai()

load_dotenv(verbose=True)

mcp_http_server = MCPServerSSE(
    url="http://127.0.0.1:8000/sse",
)

client_agent = Agent(
    "openai:gpt-4o-mini",
    mcp_servers=[mcp_http_server],
    system_prompt="You are a helpful customer service AI assistant"
)

async def main_client():
    async with client_agent.run_mcp_servers():
        prompt = "What is the weather in Accra today"
        result = await client_agent.run(prompt)
        print("Final response: ")
        print(result.output)

if __name__ == "__main__":
    asyncio.run(main_client())
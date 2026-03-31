import os
import logging
import google.cloud.logging
from dotenv import load_dotenv
from google.adk import Agent
from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()

model_name = os.getenv("MODEL")

wikipedia_tool = LangchainTool(
    tool=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
)

root_agent = Agent(
    name="animind",
    model=model_name,
    description="AniMind AI Assistant",
    instruction="""
You are AniMind AI, a powerful and friendly AI assistant.

ALWAYS answer from your OWN knowledge first.
Use Wikipedia tool ONLY for extra verification.

You can answer ANYTHING:
- Cricket, IPL, Sports stats
- Bollywood, Hollywood
- Science, Math, Coding
- History, Geography
- General knowledge
- News and current events

RULES:
- NEVER say "I cannot find"
- NEVER say "I don't know"
- ALWAYS give full detailed answer
- Answer in same language user asks
- If user asks in Hindi, reply in Hindi
- If user asks in English, reply in English
    """,
    tools=[wikipedia_tool],
)
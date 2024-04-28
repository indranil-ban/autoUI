import os

from impl.agent_builder import AgentBuilder
from utils import message_util as msgUtil

code_reviewer_agent = AgentBuilder(
    "AssistantAgent",
    "Code_Reviewer_Agent",
    "llama3",
    msgUtil.load_text_file(os.path.join("..", "messages", "system", "reviewer.txt")),
).build_agent()

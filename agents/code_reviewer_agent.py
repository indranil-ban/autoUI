import os

from impl.rag_agent_builder import RagAgentBuilder
from utils import message_util as msgUtil

code_reviewer_agent = RagAgentBuilder(
    "RagAssistantAgent",
    "Code_Reviewer_Agent",
    "llama3",
    msgUtil.load_text_file(os.path.join("..", "messages", "system", "reviewer.txt")),
).build_agent()

import os

from impl.agent_builder import AgentBuilder
from utils import message_util as msgUtil

embedding_agent = AgentBuilder(
    "AssistantAgent",
    "Code_Embedder_Agent",
    "codellama",
    msgUtil.load_text_file(os.path.join("..", "messages", "system", "embedder.txt")),
).build_agent()

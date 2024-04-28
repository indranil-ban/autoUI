import os

from impl.agent_builder import AgentBuilder
from utils import message_util as msgUtil

code_writer_agent = AgentBuilder(
    "AssistantAgent",
    "Code_Writer_Agent",
    "codellama",
    msgUtil.load_text_file(os.path.join("..", "messages", "system", "writer.txt")),
).build_agent()

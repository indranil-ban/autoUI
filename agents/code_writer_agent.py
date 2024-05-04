import os

from impl.rag_agent_builder import RagAgentBuilder
from utils import message_util as msgUtil

code_writer_agent = RagAgentBuilder(
    "RagAssistantAgent",
    "Code_Writer_Agent",
    "codellama",
    msgUtil.load_text_file(os.path.join("..", "messages", "system", "writer.txt")),
).build_agent()

import os

from impl.rag_agent_builder import RagAgentBuilder
from utils import message_util as msgUtil

embedding_agent = RagAgentBuilder(
    "RagAssistantAgent",
    "Code_Embedder_Agent",
    "codellama",
    msgUtil.load_text_file(os.path.join("..", "messages", "system", "embedder.txt")),
).build_agent()

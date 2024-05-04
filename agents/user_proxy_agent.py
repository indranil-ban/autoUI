import os
from impl.rag_agent_builder import RagAgentBuilder
from utils import message_util as msgUtil
from autogen.coding import LocalCommandLineCodeExecutor  # type: ignore
import tempfile
from constants import EMBED


# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

# Create a local command line code executor.
executor = LocalCommandLineCodeExecutor(
    timeout=10,  # Timeout for each code execution in seconds.
    work_dir=temp_dir.name,  # Use the temporary directory to store the code files.
)
user_proxy_agent = RagAgentBuilder(
    "RagUserProxyAgent",
    "User_Proxy_Agent",
    "llama3",
    msgUtil.load_text_file(os.path.join("..", "messages", "system", "user.txt")),
    {"executor": executor},
    proxy=True,
    docs_path=EMBED.CONSTANTS.DOCUMENT_FILE_NAME,
).build_agent()

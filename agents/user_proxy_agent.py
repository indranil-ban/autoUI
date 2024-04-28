import os
from impl.agent_builder import AgentBuilder
from utils import message_util as msgUtil   

user_proxy_agent = AgentBuilder(
    "UserProxyAgent",
    "User_Proxy_Agent",
    "llama3",
    msgUtil.load_text_file(os.path.join("..", "messages", "system", "user.txt")),
    {"work_dir": "output", "use_docker": False},
).build_agent()

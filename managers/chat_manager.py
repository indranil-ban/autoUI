from agents import (
    code_writer_agent as coder,
    user_proxy_agent as user,
    code_reviewer_agent as reviewer,
)
from impl.chat_manager_builder import ChatManagerBuilder

chat_manager = ChatManagerBuilder(
    [
        user.user_proxy_agent,
        coder.code_writer_agent,
        reviewer.code_reviewer_agent,
    ],
    "llama3"
).build_chat_manager()

from agents import (
    embedding_agent as embedder,
    code_writer_agent as coder,
    user_proxy_agent as user,
    code_reviewer_agent as reviewer,
)
from impl.chat_manager_builder import ChatManagerBuilder

chat_manager = ChatManagerBuilder(
    [
        user.user_proxy_agent,
        embedder.embedding_agent,
        coder.code_writer_agent,
        reviewer.code_reviewer_agent,
    ],
    "llama3",
    {
        user.user_proxy_agent: [embedder.embedding_agent, user.user_proxy_agent],
        embedder.embedding_agent: [coder.code_writer_agent,user.user_proxy_agent],
        coder.code_writer_agent: [embedder.embedding_agent, user.user_proxy_agent],
        reviewer.code_reviewer_agent: [coder.code_writer_agent, user.user_proxy_agent],
    },
).build_chat_manager()

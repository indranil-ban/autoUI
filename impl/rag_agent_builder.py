from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent  # type: ignore
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent # type: ignore

from impl.agent_builder import AgentBuilder
from constants import DB, INPUT # type: ignore or

class RagAgentBuilder(AgentBuilder):
    def __init__(
        self,
        assistant,
        name,
        llm_json_file,
        system_message,
        code_execution_config=False,
        proxy=False,
        docs_path=None,
        task="code",
    ) -> None:
        super().__init__(
            assistant, name, llm_json_file, system_message, code_execution_config
        )
        self._proxy = proxy
        self._docs_path = docs_path
        self._task = task

    def build_agent(self):
        if self._proxy and self._docs_path:
            return self.get_proxy_agent()
        else:
            return self.get_assistant_agent()

    def get_proxy_agent(self):
        return RetrieveUserProxyAgent(
            name=self._name,
            human_input_mode=INPUT.MODE.HUMAN_INPUT,
            max_consecutive_auto_reply=10,
            is_termination_msg=self._is_termination_msg,
            code_execution_config=self._code_execution_config,
            retrieve_config={
                "task": self._task,
                "docs_path": self._docs_path,
                "custom_text_types": ["mdx"],
                "chunk_token_size": 2000,
                "model": self._llm_json[0]["model"],
                "client": DB.CONSTANTS.CLIENT,
                "embedding_model": DB.CONSTANTS.EMBED_MODEL,
                "collection_name": DB.CONSTANTS.COLLECTION_NAME,
                "get_or_create": True,
            },
        )

    def get_assistant_agent(self):
        return RetrieveAssistantAgent(
            name=self._name,
            human_input_mode=INPUT.MODE.HUMAN_INPUT,
            is_termination_msg=self._is_termination_msg,
            llm_config=self.get_llm_config(),
            system_message=self._system_message,
        )

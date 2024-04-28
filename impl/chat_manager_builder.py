import autogen  # type: ignore
import json
from os import path
from abstractions.chat_manager_abstractions import BaseChatManager


class ChatManagerBuilder(BaseChatManager):

    def __init__(
        self,
        agents,
        llm_json_file,
        # system_message,
        allowed_transitions,
    ) -> None:
        super().__init__()
        self._agents = agents
        self._llm_json = self.get_llm(llm_json_file)
        # self._system_message = system_message
        self.allowed_transitions = allowed_transitions

    def get_llm(self, llm_json_file):
        # Combine path construction and opening with context manager
        with open(
            path.join(path.dirname(__file__), "..", "llms", f"{llm_json_file}.json")
        ) as json_file:
            return json.load(json_file)

    def get_llm_config(self):
        return {
            "seed": 42,
            "temperature": 0,
            "timeout": 600,
            "config_list": self._llm_json,
        }

    def build_chat_manager(self):
        groupchat = autogen.GroupChat(
            messages=[],
            max_round=6,
            agents=self._agents,
            send_introductions=True,
            speaker_transitions_type="allowed",
            speaker_selection_method="round_robin",
            allowed_or_disallowed_speaker_transitions=self.allowed_transitions,
        )
        return autogen.GroupChatManager(
            groupchat=groupchat, llm_config=self.get_llm_config()
        )

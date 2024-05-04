import autogen  # type: ignore
import json
from os import path
from abstractions.chat_manager_abstractions import BaseChatManager
from constants import CHAT


class ChatManagerBuilder(BaseChatManager):

    def __init__(
        self,
        agents,
        llm_json_file,
        # system_message,
    ) -> None:
        super().__init__()
        self._agents = agents
        self._llm_json = self.get_llm(llm_json_file)
        # self._system_message = system_message

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
        self._reset_agents()
        groupchat = autogen.GroupChat(
            messages=[],
            max_round=6,
            agents=self._agents,
            send_introductions=True,
            speaker_selection_method=CHAT.CONSTANTS.SPEAKER_SELECTION_METHOD,
        )
        return autogen.GroupChatManager(
            groupchat=groupchat, llm_config=self.get_llm_config()
        )

    def _reset_agents(self):
        for agent in self._agents:
            agent.reset()

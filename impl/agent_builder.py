import autogen  # type: ignore
import json
from os import path
from abstractions.agent_abstractions import BaseAgent


class AgentBuilder(BaseAgent):

    def __init__(
        self,
        assistant,
        name,
        llm_json_file,
        system_message,
        code_execution_config=False,
    ) -> None:
        super().__init__()
        self._assistant = assistant
        self._name = name
        self._llm_json = self.get_llm(llm_json_file)
        self._system_message = system_message
        self._code_execution_config = code_execution_config
        self._is_termination_msg = lambda x: (
            x.get("content", "").rstrip().endswith("TERMINATE")
            if code_execution_config
            else False
        )

    def get_llm(self, llm_json_file):
        # Combine path construction and opening with context manager
        with open(
            path.join(path.dirname(__file__), "..", "llms", f"{llm_json_file}.json"),
            "r",
            encoding="utf-8",
        ) as json_file:
            return json.load(json_file)

    def get_llm_config(self):
        return {
            "seed": 42,
            "temperature": 0,
            "timeout": 600,
            "config_list": self._llm_json,
        }

    def build_agent(self):
        return getattr(autogen, self._assistant)(
            name=self._name,
            human_input_mode="NEVER",
            max_consecutive_auto_reply=10,
            llm_config=self.get_llm_config(),
            system_message=self._system_message,
            is_termination_msg=self._is_termination_msg,
            code_execution_config=self._code_execution_config,
        )

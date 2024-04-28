from abc import ABC, abstractmethod

# Interface to abstract methods used in the agents.
class BaseAgent(ABC):
    @abstractmethod
    def get_llm(self):
        pass

    @abstractmethod
    def get_llm_config(self):
        pass

    @abstractmethod
    def build_agent(self):
        pass
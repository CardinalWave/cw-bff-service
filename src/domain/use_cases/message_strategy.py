from abc import ABC, abstractmethod

class MessageStrategy(ABC):

    @abstractmethod
    def handle_message(self, message) -> None:
        pass

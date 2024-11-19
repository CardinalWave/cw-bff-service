from src.domain.use_cases.message_strategy import MessageStrategy
from src.domain.models.sessions import Session

class MessageHandler:

    def __init__(self, strategy: MessageStrategy, connection: any) -> None:
        self.__strategy = strategy
        self.__connection = connection

    def set_strategy(self, strategy: MessageStrategy):
        self.__strategy = strategy

    def handle(self, message) -> Session:
        return self.__strategy.handle_message(message, self.__connection)

from src.domain.use_cases.message_strategy import MessageStrategy

class MessageHandler:
    
    def __init__(self, strategy: MessageStrategy) -> None:
        self.__strategy = strategy

    def set_strategy(self, strategy: MessageStrategy):
        self.__strategy = strategy

    def handle(self, message):
        self.__strategy.handle_message(message)
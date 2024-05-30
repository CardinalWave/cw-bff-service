from src.domain.use_cases.message_strategy import MessageStrategy

class WebSocketStrategy(MessageStrategy):

    @classmethod
    def handle_message(self, message):
        print("Handling WebSocket message")


from src.domain.use_cases.message_strategy import MessageStrategy

class MqttStrategy(MessageStrategy):

    @classmethod
    def handle_message(self, message):
        print("Handling MQTT message")


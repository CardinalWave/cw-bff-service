from src.presentation.session_payload import SessionPayload
from src.main.handler.message_handler import MessageHandler
from src.data.use_cases.websocket_strategy import WebSocketStrategy
from src.data.use_cases.mqtt_strategy import MqttStrategy

class session_composer:

    def __init__(self, payload: any, message_type: str):
        if message_type == "websocket":
            payload = SessionPayload(payload).package()
            strategy = WebSocketStrategy()
        elif message_type == "mqtt":
            payload = SessionPayload(payload).package()
            strategy = MqttStrategy()
        else:
            raise ValueError("Unknowm message type")
        self.handler = MessageHandler(strategy)
        self.handle(payload)

    def handle(self, message):
        self.handler.handle(message)


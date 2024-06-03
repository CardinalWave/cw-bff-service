from src.main.handler.message_handler import MessageHandler
from src.data.use_cases.websocket_strategy import WebSocketStrategy
from src.data.use_cases.mqtt_strategy import MqttStrategy
from src.presentation.session_payload import SessionPayload
from src.data.use_cases.connection_manager import ConnecionManager
from src.domain.models.client import Client 


class SessionComposer:

    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client
        self.websocket_server = None
        self.session_id = None
        self.clients = {}
        self.connection_manager = ConnecionManager(self.clients)

    def receiver(self, message_type, message):
        if message_type == "websocket":
            strategy = WebSocketStrategy()
            session_payload = SessionPayload(message)
            method = self.mqtt_client
        elif message_type == "mqtt":
            strategy = MqttStrategy()
            session_payload = SessionPayload(message.payload)
            method = self.connection_manager
        else:
            raise ValueError("Unknowm message type")
        self.handler = MessageHandler(strategy, method)
        self._handle(session_payload)
        self.session_id = session_payload.session.session_id

    def _handle(self, session_payload):
        session_payload = self.handler.handle(session_payload)
        print(session_payload.session.session_id[0])

    def set_sockets(self, websocketserver):
        self.websocket_server = websocketserver

    def update_socket(self, active_sockets):
        self.connection_manager.update_clients(active_sockets, self.session_id)

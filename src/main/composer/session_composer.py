#pylint: disable=attribute-defined-outside-init
from src.main.handler.message_handler import MessageHandler
from src.data.use_cases.websocket_strategy import WebSocketStrategy
from src.data.use_cases.mqtt_strategy import MqttStrategy
from src.presentation.session_payload import SessionPayload
from src.data.use_cases.connection_manager import ConnectionManager
from src.main.logs.logs_interface import LogInterface


class SessionComposer:

    def __init__(self, mqtt_client, logger: LogInterface):
        self.mqtt_client = mqtt_client
        self.websocket_server = None
        self.session_id = None
        self.clients = {}
        self.connection_manager = ConnectionManager(self.clients)
        self.__logger = logger


    def receiver(self, message_type, message):
        self.__logger.log_session(session=message, action=message_type)
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

    def _handle(self, session_payload: SessionPayload):
        session_payload = self.handler.handle(session_payload)

    def set_sockets(self, websocketserver):
        self.websocket_server = websocketserver

    def update_socket(self, socket_, active_sockets, message):
        session_payload = SessionPayload(message)
        session_id = session_payload.session.session_id
        self.connection_manager.update_clients(socket_, active_sockets, session_id)

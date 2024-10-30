from abc import ABC, abstractmethod
from paho.mqtt.client import Client as mqttc
from src.domain.models.sessions import Session
from src.presentation.session_payload import SessionPayload


class MessageStrategy(ABC):

    @abstractmethod
    def handle_message(self, session_payload: SessionPayload, connection: mqttc) -> Session:
        pass

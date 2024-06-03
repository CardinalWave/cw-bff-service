from abc import ABC, abstractmethod
from src.domain.models.sessions import Session
from src.presentation.session_payload import SessionPayload

class MessageStrategy(ABC):

    @abstractmethod
    def handle_message(self, session_payload: SessionPayload, connection, clients) -> Session:
        pass

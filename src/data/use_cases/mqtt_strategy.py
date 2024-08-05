from src.domain.use_cases.message_strategy import MessageStrategy
from src.presentation.session_payload import SessionPayload
from src.data.use_cases.connection_manager import ConnectionManager


class MqttStrategy(MessageStrategy):

    def handle_message(self, session_payload: SessionPayload, connection: ConnectionManager):
        session = session_payload.session

        session_id = session.session_id

        client = connection.find_session_id(session_id[0])
        print(session_payload.package())
        connection.send_message(client, session_payload.package())

        print("Handling MQTT message")
        return session_payload

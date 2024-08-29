from paho.mqtt.client import Client as mqttc
from src.domain.use_cases.message_strategy import MessageStrategy
from src.presentation.session_payload import SessionPayload


class WebSocketStrategy(MessageStrategy):

    def handle_message(self, session_payload: SessionPayload, connection: any):
        session = session_payload.session
        session.device_id = "cloud_01"

        print("Handling WebSocket message")
        topic = "/{}/{}/{}".format(session.device_id, session.session_id, session.action)
        connection.publish(topic, session_payload.package())

        return session_payload

from paho.mqtt.client import Client as mqttc
from src.domain.use_cases.message_strategy import MessageStrategy
from src.presentation.session_payload import SessionPayload


class WebSocketStrategy(MessageStrategy):

    @classmethod
    def handle_message(self, session_payload: SessionPayload, connection: any):
        session = session_payload.session

        session.device_id = "cloud_01"

        print("Handling WebSocket message")
        topic = "/{}/{}/{}".format(session.device_id, session.session_id[0], session.action[0])
        print(session_payload.package())
        connection.publish(topic, session_payload.package())

        print(topic)
        return session_payload

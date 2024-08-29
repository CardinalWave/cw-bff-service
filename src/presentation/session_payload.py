import json
from src.domain.models.sessions import Session


class SessionPayload:

    def __init__(self, payload: str):
        self.payload = payload
        self.session = self._serialization()

    def _serialization(self):
        try:
            data = json.loads(self.payload)
            session = Session(device_id=data.get('device_id'),
                              session_id=data.get('session_id'),
                              action=data.get('action'),
                              payload=data.get('payload'))
            return session
        except Exception as error:
            pass

    @staticmethod
    def _to_json(response):
        json_payload = json.dumps(response)
        return json_payload

    def package(self):
        response = {
            "device_id": self.session.device_id,
            "session_id": self.session.session_id,
            "action": self.session.action,
            "payload": self.session.payload
        }
        return self._to_json(response)

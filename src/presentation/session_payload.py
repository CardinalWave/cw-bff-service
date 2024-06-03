import json
from src.domain.models.sessions import Session

class SessionPayload():

    def __init__(self, payload: Session):
        self.payload = payload
        self.session = self._serialization()

    def _serialization(self):
        try:
            data = json.loads(self.payload)
            session = Session(data.get('device_id'), data.get('session_id'), data.get('action'), data.get('payload'))
            return session
        except Exception as erro:
            print(erro)

    def _to_json(self, packaga_dict: any):
        json_payload = json.dumps(packaga_dict)
        return json_payload
        

    def package(self):
        response = {
                        "device_id": self.session.device_id[0],
                        "session_id": self.session.session_id[0],
                        "action": self.session.action[0],
                        "payload": self.session.payload
                    }
        return self._to_json(response)
    

    
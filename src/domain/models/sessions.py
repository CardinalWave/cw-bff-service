#pylint: disable=trailing-comma-tuple
import json

class Session:
    def __init__(self, device_id: str, session_id: str, action: str, payload: any) -> None:
        self.device_id = device_id,
        self.session_id = session_id,
        self.action = action,
        self.payload = payload

    def to_dict(self):
        return {
            "device_id": self.device_id,
            "session_id": self.session_id,
            "action": self.action,
            "payload": self.payload
        }

    
    def to_json(self):
        try:
            data = json.dumps(self.to_dict(), indent=4)
            return data
        except Exception as erro:
            print(erro)

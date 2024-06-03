#pylint: disable=trailing-comma-tuple
import json

class Client:
    def __init__(self, socket, session_id: any) -> None:
        self.socket = socket,
        self.session_id = session_id,

    def to_dict(self):
        return {
            "socket": self.socket,
            "session_id": self.session_id
        }
    
    def to_json(self):
        try:
            data = json.dumps(self.to_dict(), indent=4)
            return data
        except Exception as erro:
            print(erro)

#pylint: disable=trailing-comma-tuple
import json


class Client:
    def __init__(self, socket_id, session_id: any, socket: any) -> None:
        self.socket_id = socket_id
        self.session_id = session_id
        self.socket = socket

    def to_dict(self):
        return {
            "socket_id": self.socket_id,
            "session_id": self.session_id,
            "socket": self.socket_id
        }

    def to_json(self):
        try:
            data = json.dumps(self.to_dict(), indent=4)
            return data
        except Exception as err:
            print(err)

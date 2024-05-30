import json
from src.domain.models.sessions import Session
from src.presentation.interface.session_interface import SessionInterface

class SessionPayload(SessionInterface):

    def __init__(self, payload: any) -> Session:
        self.payload = payload

    def package(self):
        data = self.__serialization()
        session = Session(data.get('device_id'), data.get('session_Id'), data.get('action'), data.get('payload'))
        response = {
                        "device_id": "server_001",
                        "session_id": session.session_id[0],
                        "action": session.action[0],
                        "payload": session.payload
                    }

        return response
    
    def __serialization(self):
        try:
            data = json.loads(self.payload)
            print(f'DATA: ', data)
            print(data.get('session_Id'))
            return data
        except Exception as erro:
            print(erro)
        



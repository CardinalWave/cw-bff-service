from src.domain.models.client import Client
from flask import session

class ConnectionManager:
    def __init__(self, active_sockets) -> None:
        self.sockets = active_sockets
        self.clients = {}

    def update_clients(self, socket_ident: Client, active_sockets, session_id):
        print(f'New: {active_sockets}')
        print(f'Old: {self.sockets}')
        self.sockets = active_sockets
        socket_ident.session_id = session_id
        for socket, client in self.clients.items():
            if client.session_id == session_id:
                print(f'Removendo socket inativo {socket}')
                del self.clients[socket]
                break
        self.clients[socket_ident.socket] = socket_ident
        print(f'Client: {socket_ident} | socket: {socket_ident.socket_id} | socket_obj: {socket_ident.socket}')
        print(f"New connection: session_id = {socket_ident.session_id}")
        print("Clientes ativos:", self.clients)
        print("Sockets ativos:", self.sockets)
        return self.sockets


    def send_message(self, session_id, message) -> any:
        for websocket, client in self.clients.items():
            try:
                if client.session_id == session_id:
                    print(f'Client: {client} | socket: {client.socket_id} | socket_obj: {client.socket}')
                    for socket in self.sockets:
                        print(f'Websocket: {websocket}')
                        print(f'socket: {socket.__repr__()}')
                        if websocket == socket.__repr__():
                            socket.send(message)
                        else:
                            print(f'Não encontrado: {socket.__repr__()}')
                    return client
            except Exception as e:
                print(f"Erro ao enviar mensagem para o socket {client.socket_id}: {e}")

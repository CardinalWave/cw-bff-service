#pylint: disable=unnecessary-dunder-call, undefined-loop-variable, bad-indentation
from src.domain.models.client import Client

class ConnectionManager:
    def __init__(self, active_sockets) -> None:
        self.sockets = active_sockets
        self.clients = {}


    def update_clients(self, socket_ident: Client, active_sockets, session_id):
        self.sockets = active_sockets
        socket_ident.session_id = session_id
        existing_socket = None
        for socket, client in self.clients.items():
            if client.session_id == session_id:
                existing_socket = socket
                break
        if existing_socket:
            print(f'Removendo socket inativo {socket}')
            del self.clients[existing_socket]
        self.clients[socket_ident.socket] = socket_ident
        print(f'Client: {socket_ident} | socket: {socket_ident.socket_id} |'
              f'socket_obj: {socket_ident.socket}')
        print(f"New connection: session_id = {socket_ident.session_id}")
        print("Clientes ativos:", self.clients)
        print("Sockets ativos:", self.sockets)
        return self.sockets

    def send_message(self, session_id, message) -> any:
        for websocket, client in self.clients.items():
            try:
                print(f'Client: {client} | socket: {client.socket_id} |'
                      f'socket_obj: {client.socket}')
                for socket in self.sockets:
                    if client.session_id == session_id:
                        print(f'Websocket: {websocket} - Type: {websocket}')
                        print(f'socket: {socket.__repr__()} - Type: {socket.__repr__()}')
                        if websocket == socket.__repr__():
                            socket.send(message)
                        else:
                           print(f'Não encontrado: {socket.__repr__()}')
            except Exception as e:
                print(f"Erro ao enviar mensagem para o socket {client.socket_id}: {e}")

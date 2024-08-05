from src.domain.models.client import Client


class ConnectionManager:
    def __init__(self, active_sockets) -> None:
        self.sockets = active_sockets
        self.clients = {}

    def update_clients(self, active_sockets, session_id):
        self.sockets = active_sockets
        for socket in self.sockets:
            if socket not in self.clients:
                self.clients[socket] = Client(socket=socket, session_id=session_id)
                connection = self.clients[socket]
                print(f"New connection: session_id = {connection.session_id[0][0]}")
        # Remove sockets
        inactive_sockets = [socket for socket in self.clients if socket not in self.sockets]
        for socket in inactive_sockets:
            removed_client = self.clients.pop(socket)
            print(f"Conexão removida: {removed_client.socket}")

        print("Clientes ativos:", self.clients)
        print("Sockets ativos:", self.sockets)
        return self.sockets

    def find_session_id(self, session_id) -> Client:
        for websocket, client in self.clients.items():
            if client.session_id[0][0] == session_id:
                return client

    @staticmethod
    def send_message(client: Client, message):

        if client:
            socket = client.socket[0]
            socket.send(message)
            print(f"Mensagem enviada para o socket {socket}")
        else:
            print("Socket não encontrado")

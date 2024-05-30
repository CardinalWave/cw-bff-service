from flask_websockets import WebSockets
from src.main.composer.session_composer import session_composer

class WebSocketServer:
    def __init__(self, app):
        self.sockets = WebSockets(app)
        self.clients = []

        @self.sockets.on_message
        def echo(message):
            print(f"Mensagem recebida: {message}")
            session_composer(message, "websocket")
            return message

        @self.sockets.on_close
        def close(ws):
            self.clients.remove(ws)
            print("Cliente desconectado")

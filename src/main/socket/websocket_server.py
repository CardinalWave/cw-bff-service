from uuid import uuid4
from flask_websockets import WebSockets
from src.main.composer.session_composer import SessionComposer

class WebSocketServer:
    def __init__(self, app, session_composer: SessionComposer):
        self.sockets = WebSockets(app)
        self.clients = {}

        @self.sockets.on_message
        def echo(message):
            print(f"Mensagem recebida: {message}")
            session_composer.receiver("websocket", message)
            session_composer.update_socket(self.sockets.active_sockets)
            return message

        @self.sockets.on_close
        def close(ws):
            print("Cliente desconectado")

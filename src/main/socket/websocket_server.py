import socket
from uuid import uuid4
from flask import Flask, session
from flask_websockets import WebSockets, ws
from src.main.composer.session_composer import SessionComposer
from src.domain.models.client import Client


class WebSocketServer:
    def __init__(self, app, session_composer: SessionComposer):
        app.secret_key = 'sua_chave_secreta'  # Necessário para gerenciamento de sessão
        self.sockets = WebSockets(app)

        clients = {}
        socket_to_client = {}

        @self.sockets.on_open
        def handle_open():
            session['ws.ident'] = str(uuid4())
            client_id = session['ws.ident']

            socket_to_client[ws] = client_id
            clients[client_id] = ws

            print(f"Novo cliente conectado: {client_id}")

        @self.sockets.on_message
        def handle_message(message):
            print(f"Mensagem recebida: {message}")
            client_id = socket_to_client.get(ws)
            if client_id:
                session_composer.receiver("websocket", message)
                socket_ = Client(socket_id=client_id, socket=ws.__repr__(), session_id="")
                session_composer.update_socket(socket_, self.sockets.active_sockets, message)
                return message
            else:
                print("WebSocket não encontrado para a mensagem")

        @self.sockets.on_close
        def close(ws):
            print("Cliente desconectado")

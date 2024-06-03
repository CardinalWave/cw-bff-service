import time
from uuid import uuid4
from flask import Flask, jsonify, request, render_template
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from src.main.socket.websocket_server import WebSocketServer
from src.main.mqtt.mqtt_connection import MQTTClient
from src.main.composer.session_composer import SessionComposer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    mqtt_client = MQTTClient("localhost", 1883)
    mqtt_client.connect()

    if mqtt_client.connected:
        
        server = pywsgi.WSGIServer(('localhost', 5000), app, handler_class=WebSocketHandler)
        session_composer = SessionComposer(mqtt_client.client)
        mqtt_client.set_session_composer(session_composer)
        sockets = WebSocketServer(app, session_composer)
        session_composer.set_sockets(sockets)
        print("Servidor WebSocket iniciado em ws://localhost:5000/")
        server.serve_forever()

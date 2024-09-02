import os
import threading

from flask import Flask, render_template
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from src.main.socket.websocket_server import WebSocketServer
from src.main.mqtt.mqtt_connection import MQTTClient
from src.main.composer.session_composer import SessionComposer
from src.config.config import Config

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # local_ip = os.getenv('LOCAL_IP')
    # flask_port = int(os.getenv('FLASK_PORT'))
    # mqtt_broker_ip = os.getenv('MQTT_BROKER_IP')
    # mqtt_broker_port = int(os.getenv('MQTT_BROKER_PORT'))
    local_ip = Config.CW_BFF_SERVICE_IP
    flask_port = int(Config.CW_BFF_SERVICE_PORT)
    mqtt_client = MQTTClient(Config.MQTT_BROKER_IP, Config.MQTT_BROKER_PORT)
    mqtt_client.connect()

    if mqtt_client.connected:
        server = pywsgi.WSGIServer((local_ip, flask_port), app, handler_class=WebSocketHandler)
        session_composer = SessionComposer(mqtt_client.client)
        mqtt_client.set_session_composer(session_composer)
        sockets = WebSocketServer(app, session_composer)
        session_composer.set_sockets(sockets)
        print(f"Servidor WebSocket iniciado em ws://{local_ip}:{flask_port}/")
        server.start()
        server.serve_forever()

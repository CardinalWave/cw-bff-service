from flask import Flask, render_template
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from src.main.socket.websocket_server import WebSocketServer
from src.main.mqtt.mqtt_connection import MQTTClient
from src.main.composer.session_composer import SessionComposer
from src.config.config import Config
from src.main.logs.logs import Log


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    log = Log()
    local_ip = Config.CW_BFF_SERVICE_IP
    flask_port = int(Config.CW_BFF_SERVICE_PORT)
    print(f"Trying connect to mqtt://{Config.MQTT_BROKER_IP}:{Config.MQTT_BROKER_PORT}/")
    mqtt_client = MQTTClient(Config.MQTT_BROKER_IP, Config.MQTT_BROKER_PORT)
    mqtt_client.connect()

    if mqtt_client.connected:
        print(f"Servidor WebSocket iniciado em ws://{local_ip}:{flask_port}/")
        server = pywsgi.WSGIServer((local_ip, flask_port), app, handler_class=WebSocketHandler)
        session_composer = SessionComposer(mqtt_client.client, log)
        mqtt_client.set_session_composer(session_composer)
        sockets = WebSocketServer(app, session_composer)
        session_composer.set_sockets(sockets)
        print(f"Servidor WebSocket iniciado em ws://{local_ip}:{flask_port}/")
        server.start()
        server.serve_forever()

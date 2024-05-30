import time
from flask import Flask, jsonify, request, render_template
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from src.main.socket.websocket_server import WebSocketServer
from src.main.mqtt.mqtt_connection import mqttc, on_connect, on_message, on_publish

app = Flask(__name__)
sockets = WebSocketServer(app)

clients = []

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":

    mqtt_broker_ip = "localhost"
    mqtt_broker_port = 1883

    connected = False

    while not connected:
        try:
            print("Connecting")
            mqttc.connect(mqtt_broker_ip, mqtt_broker_port, 60)
            mqttc.subscribe("#");
            mqttc.on_connect = on_connect
            mqttc.on_message = on_message
            mqttc.on_publish = on_publish
            mqttc.loop_start()
            connected = True
        except Exception as e:
            print(f"Falha na conexao: {e}")
            time.sleep(5)

    server = pywsgi.WSGIServer(('localhost', 5000), app, handler_class=WebSocketHandler)
    print("Servidor WebSocket iniciado em ws://localhost:5000/")
    server.serve_forever()

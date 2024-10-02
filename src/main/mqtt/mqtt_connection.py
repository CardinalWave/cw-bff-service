import threading
import time
import paho.mqtt.client as mqtt
from src.main.composer.session_composer import SessionComposer
from src.config.config import Config


class MQTTClient:
    def __init__(self, broker_ip=Config.MQTT_BROKER_IP,
                 broker_port=Config.MQTT_BROKER_PORT):
        self.broker_ip = broker_ip
        self.broker_port = int(broker_port)
        self.client = mqtt.Client()
        self.connected = False

        # Assign the callback functions
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.session_composer = None

    def set_session_composer(self, session_composer: SessionComposer):
        self.session_composer = session_composer

    @staticmethod
    def on_connect(self, client, userdata, flags):
        print("Connected")

    def on_message(self, client, userdata, msg):
        print(f"Mensagem recebida: {msg}")
        self.session_composer.receiver("mqtt", msg)
        pass

    def on_publish(self, client, userdata, result):
        pass

    def connect(self):
        while not self.connected:
            try:
                print(f"Connecting mqtt://{self.broker_ip}:{self.broker_port} - port_type {type(self.broker_port)}")
                self.client.connect(self.broker_ip, self.broker_port, 60)
                self.connected = True
                self.client.subscribe("/server/#")
                client_thread = threading.Thread(target=self.client.loop_start(), daemon=True)
                client_thread.start()
            except Exception as e:
                print(f"Falha na conexao: {e}")
                time.sleep(5)

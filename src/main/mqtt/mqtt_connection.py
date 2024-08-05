import threading
import time
import paho.mqtt.client as mqtt
from src.main.composer.session_composer import SessionComposer


class MQTTClient:
    def __init__(self, broker_ip="192.168.15.69", broker_port=1883):
        self.broker_ip = broker_ip
        self.broker_port = broker_port
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
                print("Connecting")
                self.client.connect(self.broker_ip, self.broker_port, 60)
                self.connected = True
                self.client.subscribe("/server/#")
                client_thread = threading.Thread(target=self.client.loop_start(), daemon=True)
                client_thread.start()
            except Exception as e:
                print(f"Falha na conexao: {e}")
                time.sleep(5)

#pylint: disable=unused-argument
import json
import paho.mqtt.client as mqtt
from src.main.composer.session_composer import session_composer

def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")

def on_message(client, userdata, msg):
    session_composer(msg.payload, "mqtt")

def on_publish(client, userdata, result):
    pass

mqttc = mqtt.Client()

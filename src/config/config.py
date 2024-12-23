import configparser
import os


class Config:
    config = configparser.ConfigParser()
    config.read('src/config/config.ini')

    MQTT_BROKER_IP = config.get('MQTT', 'IP')
    MQTT_BROKER_PORT = config.getint('MQTT', 'PORT')
    MQTT_TIMESTAMP = os.getenv('MQTT', 'MQTT_TIMESTAMP')
    CW_BFF_SERVICE = config['CW_BFF_SERVICE']['BaseURL']
    CW_BFF_SERVICE_IP = config['CW_BFF_SERVICE']['IP']
    CW_BFF_SERVICE_PORT = config['CW_BFF_SERVICE']['PORT']
    CW_BFF_SERVICE_URL = config['CW_BFF_SERVICE']['BaseURL']
    CW_LOG_TRACE = config['CW_LOG_TRACE']['BaseURL']
    CW_LOG_TRACE_IP = config['CW_LOG_TRACE']['IP']
    CW_LOG_TRACE_PORT = config['CW_LOG_TRACE']['PORT']

    # From Dockerfile
    MQTT_BROKER_IP = os.getenv('MQTT_BROKER_IP', MQTT_BROKER_IP)
    MQTT_BROKER_PORT = int(os.getenv('MQTT_BROKER_PORT', MQTT_BROKER_PORT))
    MQTT_TIMESTAMP = os.getenv('MQTT_TIMESTAMP', MQTT_TIMESTAMP)
    CW_BFF_SERVICE = os.getenv('CW_BFF_SERVICE', CW_BFF_SERVICE)
    CW_BFF_SERVICE_IP = os.getenv('CW_BFF_SERVICE_IP', CW_BFF_SERVICE_IP)
    CW_BFF_SERVICE_PORT = int(os.getenv('CW_BFF_SERVICE_PORT', CW_BFF_SERVICE_PORT))
    CW_BFF_SERVICE_URL = os.getenv('CW_BFF_SERVICE_URL', CW_BFF_SERVICE_URL)
    CW_LOG_TRACE = os.getenv('CW_LOG_TRACE', CW_LOG_TRACE)
    CW_LOG_TRACE_IP = os.getenv('CW_LOG_TRACE_IP', CW_LOG_TRACE_IP)
    CW_LOG_TRACE_PORT = int(os.getenv('CW_LOG_TRACE_PORT', CW_LOG_TRACE_PORT))

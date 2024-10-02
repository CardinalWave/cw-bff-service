# Use a imagem base do Python
FROM python:3.11-alpine

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as propriedades necessarias
RUN apk add --no-cache git build-base libffi-dev

# Atualiza as dependencias
RUN python3 -m pip install --upgrade pip

# Instala as dependências do Pythonz
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Define variáveis de ambiente para o IP e porta do MQTT
ENV MQTT_BROKER_IP=mqtt-mosquitto
ENV MQTT_BROKER_PORT=1883
ENV MQTT_TIMESTAMP=60
ENV CW_BFF_SERVICE=cw-bff-service
ENV CW_BFF_SERVICE_IP=0.0.0.0
ENV CW_BFF_SERVICE_PORT=5004
ENV CW_LOG_TRACE_IP=cw-log-trace
ENV CW_LOG_TRACE_PORT=5050

# Expor a porta 5004 para o WebSocket
EXPOSE 5004

# Comando para executar a aplicação Flask
CMD ["python", "main.py"]
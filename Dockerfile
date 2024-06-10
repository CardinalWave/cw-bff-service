# Use a imagem base do Python
FROM python:3.11-alpine    

# Instale as dependecias do sistema
#RUN apt-get update && \ 
#    apt-get install -y git && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*s|

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

RUN apk add --no-cache git build-base

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Define variáveis de ambiente para o IP e porta do MQTT
ENV MQTT_BROKER_IP=192.168.12.1
ENV MQTT_BROKER_PORT=1883
ENV LOCAL_IP=172.17.0.2
ENV FLASK_PORT=5000

# Expor a porta 5000 para o Flask
EXPOSE 5000

# Comando para executar a aplicação Flask
CMD ["python", "main.py"]

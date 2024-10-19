# CW-Central-Service

## API - Servico de controle central do sistema CardinalWave
https://github.com/CardinalWave/cw-bff-service.git

## Desenvolved with:
    - Python 3.11
    - Flask 3.0
	- Paho 1.6.1


## About
Assembly Votes is an API under development, focused on facilitating the creation of voting sessions in polls 
CW-Bff Service e uma API em desenvolvimento constante, seu prinicipal objetivo e enviar o arquivo html para a requisicoes vindas do http://cardinalwave.net alem de realizar a transformacoes das requisicoes dos usuarios (quando conectados diretamente no server) de WebSocket para Mqtt, para prosseguirem no sistema.

- Facilidade de alteracao
- Integração com placas ESP
- Usabilidade simplificada


### Config
 - Incializaçao com docker-compose
    - Main route: http://localhost:5004/
    - Port: 5004
    - Mqtt:
	- mqtt-mosquitto
        - mqtt://localhost:1883

# Projeto 🚧
## Esse projeto tem como base para seu modelo sistemas  como DDD (Domain Drive Desingn) e TDD (Test Driven Design)

    src
    ├── config                   # Arquivos de configuracao local 
    ├── data                    # Implementacoes separadas por casos de uso
    ├── domain                     # Interfaces separadas por casos de uso
    ├── infra                    # Implementacoes relacionadas a bancos de dados e acesso a api de autenticacao
    ├── presentation                   # Implementacoes relacionadas as entradas da API 
    ├── main                   # Rotas e Composer dos casos de uso e envio de logs
    ├── test                   # Testes do sistema
	├── Dockerfile                   # Arquivo de configuracao do servico Docker
	└── run.py       # Arquivo de execucao

# Rotas ⛕

# Usuario
### Entrar no usuario
| Method | Route | 
| ------------- | ------------- |
|POST           | /user/login | VOID

Realiza o login do usuario

    "email" : "teste@outlook.com",
    "password" : "password", 
    "session_id" : "session_idxxxxxxxx"
	"device": "espxxxx"


### Sair do sistema
| Method | Route | 
| ------------- | ------------- |
|POST           | /user/logout | VOID

Realiza o logout do usuario no sistema

    "token" : "xxxxx-xxxxx-xxxxx",
    "email" : "teste@outlook.com", 
    "username" : "username"

### Register usuario
| Method | Route | 
| ------------- | ------------- |
|POST           | /user/register | VOID

Realiza o registro do usuario no sistema

    "email" : "teste@outlook.com", 
    "username" : "username",
	"password" : "password"

# CHAT
### Entrar no chat
| Method | Route | 
| ------------- | ------------- |
|POST           | /chat/join | VOID

Sinaliza para o restante do sistema que o usuario deu entrada em um chat disponivel

    "token" : "xxxx-xxxx-xxxx", 
    "group_id" : "group_id"



### Sair do chat
| Method | Route | 
| ------------- | ------------- |
|POST           | /chat/leave| VOID

Sinaliza para o restante do sistema que o usuario saiu do chat em que estava

    "token" : "xxxx-xxxx-xxxx"


### Enviar mensagem
| Method | Route | 
| ------------- | ------------- |
|POST           | /chat/send| VOID

Sinaliza para o restante do sistema a mensage enviada pelo usuario para o grupo em questao

    "token" : "xxxx-xxxx-xxxx",
	"group_id": "group_id",
	"message" : "message"

# GROUP
### Criar grupo
group_routes.group_create  POST     /group/create          
| Method | Route | 
| ------------- | ------------- |
|POST           | /group/create | VOID

Realiza a criacao de um grupo

    "title" : "xxxx-xxxx-xxxx"

### Entrar no grupo
| Method | Route | 
| ------------- | ------------- |
|POST           | /group/join| VOID

Realiza a insercao do usuario em um grupo

    "token" : "xxxx-xxxx-xxxx",
	"group_id" : "group_id"

### Sair do grupo
| Method | Route | 
| ------------- | ------------- |
|POST           | /group/join| VOID

Realiza a insercao do usuario em um grupo

    "token" : "xxxx-xxxx-xxxx",
	"group_id" : "group_id"

### Listar Grupos (Usuario)
| Method | Route | 
| ------------- | ------------- |
|POST           | /group/join| VOID

Listar grupos que o usuario tem acesso

    "token" : "xxxx-xxxx-xxxx",


#### References

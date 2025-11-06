from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Configuração de conexão com o MongoDB (serviço 'mongodb' definido no docker-compose)
app.config['MONGODB_SETTINGS'] = {
    'db': 'users', 
    'port': 27017,
    'host': 'mongodb',
    'username': 'admin',
    'password': 'admin' # Senha definida no docker-compose.yml
}

# Inicializa o MongoEngine com as configurações do app
db = MongoEngine(app) 

# Inicializa o RequestParser para lidar com dados de entrada (JSON ou formulário)
_user_parser = reqparse.RequestParser() 
_user_parser.add_argument('name')

# Exemplo de uso da classe Api (será necessário para definir rotas)
# api = Api(app)
# api.add_resource(User, '/users')

if __name__ == '__main__':
    # Roda a aplicação Flask na porta 5000 e host 0.0.0.0 para acesso externo no container
    app.run(host='0.0.0.0', port=5000)
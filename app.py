from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

#Configure o URL do MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/meuBancoDeDados"

mongo = PyMongo(app)

#Rota para criar um novo item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    if data:
        item_id = mongo.db.items.insert_one(data).inserted_id
        return jsonify({"id": str(item_id)}), 201
    return jsonify({"error": "Nenhum dado fornecido"}), 400

# Rota para listar todos os itens
@app.route('/items', methods=['GET'])
def get_items():
    items = mongo.db.items.find()
    result = [{"id": str(item["_id"]), "name": item["name"]} for item in items]
    return jsonify(result), 200

#Rota para atualizar um item
@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
    data = request.json
    if data:
        result = mongo.db.items.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.matched_count:
            return jsonify({"message": "Item atualizado com sucesso"}), 200
        return jsonify({"error": "Item não encontrado"}), 404
    return jsonify({"error": "Nenhum dado fornecido"}), 400

# Rota para deletar um item
@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    result = mongo.db.items.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"message": "Item deletado com sucesso"}), 200
    return jsonify({"error": "Item não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import re
import json
import uuid
import os
import pprint

#Connecting to database ---------------------------------------------------
my_secret = os.environ['MONGODB_PWD']
connection_string = f"mongodb+srv://enzotresmediano:{my_secret}@cluster0.hrke9xw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

#dbs = client.list_database_names()
#print(dbs)
#These two lines above can be uncommented to see all databases^^^
tarefas_db = client["tarefas"]
#collections = tarefas_db.list_collection_names()
#print(collections)
#These two lines above can be uncommented to see all collections^^^
#collection = tarefas_db["tarefas"]
#tarefas = collection.find()
#print(list(tarefas))

#Creating app -------------------------------------------------------------
app = Flask(__name__)


#Classes ------------------------------------------------------------------
class JSONEncoder(json.JSONEncoder):

  def default(self, o):
    if isinstance(o, ObjectId):
      return str(o)
    return json.JSONEncoder.default(self, o)


#Functions ----------------------------------------------------------------


@app.route("/tarefas", methods=["GET"])
def read():
  try:
    collection = tarefas_db["tarefas"]
    tarefas = []
    for el in collection.find():
      tarefas.append(el)
  #list() nao funciona com mongodb ent useu for loop
  except Exception as e:
    return {"message": str(e)}, 400
  #print(JSONEncoder().encode(tarefas))
  return JSONEncoder().encode(tarefas), 200


@app.route('/tarefas', methods=["POST"])
def create():
  collection = tarefas_db["tarefas"]
  try:
    
    item = request.json
    titulo = item["titulo"]
    descricao = item["descricao"]
    status = item["status"]
    dataEntrega = item["data-entrega"]
    tarefas = []
    for el in collection.find():
      print(el)
      if ("titulo") in el and titulo == el["titulo"]:
        print("POST was declined")
        return {"message": "Titulo already exists"}, 400
      tarefas.append(el)
    print("POST let through")
    #print(tarefas)
    item = {
      "titulo": titulo,
      "descricao": descricao,
      "status": status,
      "data-entrega": dataEntrega
    }
    inserted_id = collection.insert_one(item).inserted_id
    #The .inserted_id lets us see the value of the new id created for the item
    print(inserted_id)
    return JSONEncoder().encode(item), 201

  except Exception as e:
    return {"message": str(e)}, 400


@app.route('/tarefas', methods=["PUT"])
def update():
  try:
    item = request.json
    id = item["_id"]
    collection = tarefas_db["tarefas"]
    _id = ObjectId(id)
    collection.update_one(
      {"_id": _id},
      {
        "$set": {
          "titulo": item["titulo"],
          "descricao": item["descricao"],
          "status": item["status"],
          "data-entrega": item["data-entrega"]
        }
      },
    )
    item = collection.find_one({"_id": _id})
  except Exception as e:
    return {"message": str(e)}, 400

  return JSONEncoder().encode(item), 201


@app.route('/tarefas/<string:id>', methods=["DELETE"])
def delete(id):
  try:
    collection = tarefas_db["tarefas"]
    _id = ObjectId(id)
    collection.delete_one({"_id": _id})
  except Exception as e:
    return {"message": str(e)}, 400

  return {"message": f"{id} succesfully deleted"}, 400


#To run the app -----------------------------------------------------------
app.run(host='0.0.0.0', port=81)

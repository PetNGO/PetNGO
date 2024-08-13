
import pymongo 

client = pymongo.MongoClient("mongodb+srv://akhileshpatil12168:48586566@petngo.nwv97.mongodb.net/")

db= client["PetNgo"]
pet_collection = db["Pet"]
user_collection = db["User"]

def create(data):
    data = dict(data)
    response = pet_collection.insert_one(data)
    return response.inserted_id

def create_user(data):
    data = dict(data)
    response = user_collection.insert_one(data)
    return response.inserted_id

def all():
    response = pet_collection.find({})
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

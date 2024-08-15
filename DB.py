import pymongo
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError

client = pymongo.MongoClient("mongodb+srv://akhileshpatil12168:48586566@petngo.nwv97.mongodb.net/")

db = client["PetNgo"]
pet_collection = db["Pet"]
user_collection = db["User"]

def create_pet(data):
    try:
        data = dict(data)
        response = pet_collection.insert_one(data)
        return str(response.inserted_id)
    except PyMongoError:
        return "something went wrong"

def create_user(data):
    try:
        data = dict(data)
        response = user_collection.insert_one(data)
        return str(response.inserted_id)
    except PyMongoError:
        return "something went wrong"

def all():
    try:
        response = pet_collection.find({})
        data = []
        for i in response:
            i["_id"] = str(i["_id"])
            data.append(i)
        return data
    except PyMongoError:
        return "something went wrong"

def pet_info(pet_id):
    try:
        response = pet_collection.find_one({"_id": ObjectId(pet_id), "isDeleted": False})
        if response is None:
            return {"error": "Pet not found"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response
    except PyMongoError:
        return "something went wrong"

def update_pet_info(pet_id: str, data: dict):
    try:
        response = pet_collection.find_one_and_update(
            {"_id": ObjectId(pet_id)},
            {"$set": data},
            return_document=True
        )
        if response is None:
            return {"error": "Pet not found"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response
    except PyMongoError:
        return "something went wrong"

def delete_pet(pet_id: str):
    try:
        response = pet_collection.find_one_and_update(
            {"_id": ObjectId(pet_id)},
            {"$set": {"isDeleted": True}}
        )
        if response is None:
            return {"error": "something went wrong"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response
    except PyMongoError:
        return "something went wrong"

# User

def User_info(User_id: str):
    try:
        response = user_collection.find_one({"_id": ObjectId(User_id), "isDeleted": False})
        if response is None:
            return {"error": "User not found"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response
    except PyMongoError:
        return "something went wrong"

def update_User_info(user_id: str, data: dict):
    try:
        response = user_collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": data},
            return_document=True
        )
        if response is None:
            return {"error": "User not found"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response
    except PyMongoError:
        return "something went wrong"

def delete_User(User_id: str):
    try:
        response = user_collection.find_one_and_update(
            {"_id": ObjectId(User_id)},
            {"$set": {"isDeleted": True}}
        )
        if response is None:
            return {"error": "something went wrong"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response
    except PyMongoError:
        return "something went wrong"

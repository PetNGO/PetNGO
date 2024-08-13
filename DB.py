
import pymongo 
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError

client = pymongo.MongoClient("mongodb+srv://akhileshpatil12168:48586566@petngo.nwv97.mongodb.net/")

db= client["PetNgo"]
pet_collection = db["Pet"]
user_collection = db["User"]


def create_pet(data):
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


def pet_info(pet_id):
 
        print(pet_id)
        response = pet_collection.find_one({"_id": ObjectId(pet_id), "isDeleted": False})
        print(response)
        if response is None:
            return {"error": "Pet not found"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response
  
def update_pet_info(pet_id: str, data: dict):
        response = pet_collection.find_one_and_update( {"_id": ObjectId(pet_id)}, {"$set": data}, return_document=True)
        if response is None:
            return {"error": "Pet not found"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response   

  
def delete_pet(pet_id: str):
        response = pet_collection.find_one_and_update( {"_id": ObjectId(pet_id)}, {"$set": {"isDeleted": True}})
        if response is None:
            return {"error": "something went wrong"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response   
    
    
#User

def User_info(User_id):
 
        response = user_collection.find_one({"_id": ObjectId(User_id), "isDeleted": False})
        if response is None:
            return {"error": "User not found"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response
  
def update_User_info(user_id: str, data: dict):
        response = user_collection.find_one_and_update( {"_id": ObjectId(user_id)}, {"$set": data}, return_document=True)
        if response is None:
            return {"error": "User not found"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response   

  
def delete_User(User_id: str):
        response = user_collection.find_one_and_update( {"_id": ObjectId(User_id)}, {"$set": {"isDeleted": True}})
        if response is None:
            return {"error": "something went wrong"}
        
        # Convert ObjectId to string
        if "_id" in response:
            response["_id"] = str(response["_id"])

        return response  
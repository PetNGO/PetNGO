import jwt.exceptions
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

from bson.objectid import ObjectId
from pymongo.errors import PyMongoError
import bcrypt 
import jwt 

from datetime import datetime


try:
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    
    uri = config["mogoDB"]["mongoURI"]
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["PetNgo"]
pet_collection = db["Pet"]
user_collection = db["User"]
logins_collection = db["logins"]

def create_pet(data):
    try:
        
        data = dict(data)
        
        response = pet_collection.insert_one(data)
        return str(response.inserted_id)
    except PyMongoError:
        return "something went wrong"

def create_user(data):
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
            
        data = dict(data)
        
        bytes = data["password"].encode(config["bcrypt"]["encode_type"]) 
        salt = bcrypt.gensalt(config["encode_type"]["salt"])
        data["password"] = bcrypt.hashpw(bytes, salt)  
        
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

def login_user(data: dict):
    try:
        print("hello")
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
        
        response = user_collection.find_one({"email":data["email"]})
        if response is None:
            return {"error": "email or password is wrong."}
      
        if "_id" in response:
            response["_id"] = str(response["_id"])
            
        userBytes = data["password"].encode(config["bcrypt"]["encode_type"]) 
        result = bcrypt.checkpw(userBytes, response["password"]) 
        if(result is False):
            return {"message": "email or password is wrong."}
        
        ct = datetime.now()
        ts = ct.timestamp() + (5)
        
        bytes = response["_id"].encode(config["bcrypt"]["encode_type"]) 
        salt = bcrypt.gensalt(config["bcrypt"]["salt"])
        hased_user_id=  bcrypt.hashpw(bytes, salt)
        
        payload = {"userId":  str(hased_user_id) ,"exp":ts}
        encoded_jwt = jwt.encode(payload, config["jwt"]["secret"], algorithm=config["jwt"]["algorithm"])
        save_token = logins_collection.find_one_and_update({"userId":response["_id"]},{"$set":{"token":encoded_jwt, "loginTime": ct}}, upsert=True)
        print(save_token)
        
        return {"message":"logged in successfully","token":encoded_jwt}
        
    except Exception as e:
        print({"error":e})
        return  e
    
def test_token(data, token):
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
        print(token)
        decoded_token = jwt.decode(token, config["jwt"]["secret"], algorithms=config["jwt"]["algorithm"], options={"verify_exp": False}  )
        print(decoded_token)
        return decoded_token
    except jwt.exceptions.ExpiredSignatureError as e:
        return("error",str(e))
    except Exception as e:
        print(e)
        return{"error": e}

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

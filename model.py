from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime

class Pet(BaseModel):
    name:str
    age:int
    type:str
    description:str
    sex:str
    isDeleted: bool = False
    
class User(BaseModel):
    name:str
    phone:int
    email:str
    password:str
    isDeleted: bool = False
    
class UserLogings(BaseModel):
    userId: str
    token: str
    loginTime: datetime
    
    
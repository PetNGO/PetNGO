from pydantic import BaseModel

class Pet(BaseModel):
    name:str
    age:int
    type:str
    description:str
    sex:str
    
class User(BaseModel):
    name:str
    phone:int
    email:str
    password:str
    
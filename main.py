from fastapi import FastAPI

import DB
import model
app = FastAPI()

@app.get("/")
def root():
    return{"m":"hello"}

@app.post("/regi")
def create(data:model.User):
    id  = DB.create_user(data)
    return{"id":id}

@app.get("/all/pets")
def get_pets():
    data = DB.all()
    return{"data":data}


@app.post("/create-pet")
def create_pet(data:model.Pet):
    id  = DB.create_pet(data)
    return{"id":id}

@app.get("/pet/{petid}")
def get_pet_info(petid):
    id = DB.pet_info(petid)
    return{"petinfo": id}


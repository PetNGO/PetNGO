from fastapi import FastAPI, Body

import DB
import model
app = FastAPI()

# @app.get("/")
# def root():
#     return{"m":"hello"}


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
    data = DB.pet_info(petid)
    return{"petinfo": data}

@app.put("/pet/{petid}/update")
def update_pet_info(petid: str, data: dict = Body(...)):
    data = DB.update_pet_info(petid,data)
    return {"updated_data": data}

@app.delete("/pet/{petid}")
def delete_pet(petid: str,):
    data = DB.delete_pet(petid)
    return {"data deleted"}



# USer

@app.post("/regi")
def create(data:model.User):
    id  = DB.create_user(data)
    return{"id":id}

@app.get("/user/{userid}")
def get_user_info(userid):
    data = DB.User_info(userid)
    return{"userinfo": data}

@app.put("/user/{userid}/update")
def update_user_info(userid: str, data: dict = Body(...)):
    data = DB.update_User_info(userid,data)
    return {"updated_data": data}

@app.delete("/user/{userid}")
def delete_user(userid: str,):
    data = DB.delete_User(userid)
    return {"User deleted"}
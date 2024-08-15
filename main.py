from fastapi import FastAPI, Body, HTTPException
import DB
import model

app = FastAPI()

# @app.get("/")
# def root():
#     return {"m": "hello"}

@app.get("/all/pets")
def get_pets():
    try:
        data = DB.all()
        return {"data": data}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.post("/create-pet")
def create_pet(data: model.Pet):
    try:
        id = DB.create_pet(data)
        return {"id": id}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.get("/pet/{petid}")
def get_pet_info(petid: str):
    try:
        data = DB.pet_info(petid)
        return {"petinfo": data}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.put("/pet/{petid}/update")
def update_pet_info(petid: str, data: dict = Body(...)):
    try:
        updated_data = DB.update_pet_info(petid, data)
        return {"updated_data": updated_data}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.delete("/pet/{petid}")
def delete_pet(petid: str):
    try:
        DB.delete_pet(petid)
        return {"message": "data deleted"}
    except Exception:
        raise HTTPException(detail="something went wrong")

# User

@app.post("/regi")
def create_user(data: model.User):
    try:
        id = DB.create_user(data)
        return {"id": id}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.get("/user/{userid}")
def get_user_info(userid: str):
    try:
        data = DB.User_info(userid)
        return {"userinfo": data}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.put("/user/{userid}/update")
def update_user_info(userid: str, data: dict = Body(...)):
    try:
        updated_data = DB.update_User_info(userid, data)
        return {"updated_data": updated_data}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.delete("/user/{userid}")
def delete_user(userid: str):
    try:
        DB.delete_User(userid)
        return {"message": "User deleted"}
    except Exception:
        raise HTTPException(detail="something went wrong")

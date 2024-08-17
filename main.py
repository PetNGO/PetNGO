from fastapi import FastAPI, Body, HTTPException
import uvicorn
import DB
import model

app = FastAPI()

@app.get("/all/pets")
async def get_pets():
    try:
        data = await DB.all()
        return {"data": data}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.post("/create-pet")
async def create_pet(data: model.Pet):
    try:
        id = await DB.create_pet(data)
        return {"id": id}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.get("/pet/{petid}")
async def get_pet_info(petid: str):
    try:
        data = await DB.pet_info(petid)
        return {"petinfo": data}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.put("/pet/{petid}/update")
async def update_pet_info(petid: str, data: dict = Body(...)):
    try:
        updated_data = await DB.update_pet_info(petid, data)
        return {"updated_data": updated_data}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.delete("/pet/{petid}")
async def delete_pet(petid: str):
    try:
        await DB.delete_pet(petid)
        return {"message": "data deleted"}
    except Exception:
        raise HTTPException(detail="something went wrong")

# User

@app.post("/regi")
async def create_user(data: model.User):
    try:
        id = await DB.create_user(data)
        return {"id": id}
    except Exception:
        raise HTTPException(detail="something went wrong")
    
@app.post("/login")
def login_user(data: dict = Body(...)):
    try:
        print(data)
        response = DB.login_user(data)
        return response
    except  Exception as e:
        print(e)
    

@app.get("/user/{userid}")
async def get_user_info(userid: str):
    try:
        data = await DB.User_info(userid)
        return {"userinfo": data}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.put("/user/{userid}/update")
async def update_user_info(userid: str, data: dict = Body(...)):
    try:
        updated_data = await DB.update_User_info(userid, data)
        return {"updated_data": updated_data}
    except Exception:
        raise HTTPException(detail="something went wrong")

@app.delete("/user/{userid}")
async def delete_user(userid: str):
    try:
        await DB.delete_User(userid)
        return {"message": "User deleted"}
    except Exception:
        raise HTTPException(detail="something went wrong")


if __name__ == "__main__":
    uvicorn.run(app=app)
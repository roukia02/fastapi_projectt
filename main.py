from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()
users = []

@app.get("/")
def root():
    return {"Message": f"{users}"}

@app.post("/adduser")
def create_item(tomasz: dict = Body(...)):
    users.append(tomasz)
    return {f"User created, NAME: {tomasz['name']}, AGE: {tomasz['age']}"}

@app.get("/{number}")
def get_user(number: int):
    return {"Message": f"{users[number]}"}
from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()
items = []
users = []
orders = []

@app.get("/")
def root():
    return {"Message": f"{items}"}

@app.post("/additem")
def create_item(tomasz: dict = Body(...)):
    items.append(tomasz)
    return {f"Item created, NAME: {tomasz['name']}, QTY: {tomasz['quantity']}"}

@app.get("/users")
def get_users():
    return {"Message": f"{users}"}

@app.post("/adduser")
def add_user(user: dict = Body(...)):
    users.append(user)
    return {f"User created, NAME: {user['name']}, AGE: {user['age']}"}

@app.get("/orders")
def get_orders():
    return {"Message": f"{orders}"}

@app.post("/addorder")
def add_order(order: dict = Body(...)):
    orders.append(order)
    return {f"Order created, PRODUCT: {order['product']}, QTY: {order['quantity']}"}
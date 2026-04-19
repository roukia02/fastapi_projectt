from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Message": "Hello World!"}

@app.post("/createpost")
def create_post():
    return {"Message": "Post created!"}

@app.post("/createitem")
def create_item():
    return {
        "id": 1,
        "name": "Wireless Headphones",
        "price": 89.99,
        "category": "Electronics",
        "rating": 4.5
    }

@app.post("/createuser")
def create_user():
    return {
        "id": 101,
        "name": "Jane Smith",
        "email": "jane.smith@email.com",
        "country": "United States",
        "memberSince": "2023-06-15",
        "totalOrders": 12
    }

@app.post("/createorder")
def create_order():
    return {
        "id": 501,
        "userId": 101,
        "product": "Wireless Headphones",
        "total": 89.99,
        "status": "shipped",
        "createdAt": "2026-02-10T14:32:00Z"
    }

@app.post("/createbook")
def create_book():
    return {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic Fiction",
        "price": 12.99,
        "stock": 50
    }

@app.post("/createmember")
def create_member():
    return {
        "id": 201,
        "name": "Roukia Zaiter",
        "email": "roukia@library.com",
        "memberSince": "2024-01-10",
        "borrowedBooks": 3
    }

@app.post("/createborrow")
def create_borrow():
    return {
        "id": 301,
        "memberId": 201,
        "bookTitle": "The Great Gatsby",
        "borrowedAt": "2026-04-01",
        "returnDue": "2026-04-15",
        "status": "active"
    }
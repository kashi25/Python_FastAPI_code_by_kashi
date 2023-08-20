# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI
# data = []

# class Book(BaseModel):
#     id:int
#     title:str
#     author:str
#     publisher:str
    
# @app.post("/book")
# def add_book(book: Book):
#     data.append(book.model_dump())
#     return data

# @app.get("/title")
# def get_book():
#     return data

# @app.delete("/book/{id}")
# def delete_book(id: int):
#     data.pop(id-1)
#     return data



from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
data = []

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    
@app.post("/book")
def add_book(book: Book):
    data.append(book)
    return data

@app.get("/title")
def get_book(book: Book):
    return data

@app.delete("/book/{id}")
def delete_book(id: int):
    if 1 <= id <= len(data):
        data.pop(id - 1)
        return data
    else:
        return {"error": "Book not found"}

# # Run the app
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)

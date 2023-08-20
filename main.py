from fastapi import FastAPI

# initalize the app
app = FastAPI()

# initializing the
@app.get("/hello")
async def root(name:str, age: int):
    return {"name": name, "age": age}


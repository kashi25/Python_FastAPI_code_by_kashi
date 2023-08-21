from fastapi import FastAPI
import models
from routes import router
from config import engine

# Database Initialization
models.Base.metadata.create_all(bind=engine)

# Instantiate the FastAPI
app = FastAPI()


# Defining path operation for root endpoint
@app.get("/")
async def Home():
    return{"Welcome to pain patient default  main route"}

app.include_router(router)

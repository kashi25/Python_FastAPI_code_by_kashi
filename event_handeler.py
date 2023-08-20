from fastapi import FastAPI
import datetime

app = FastAPI()
@app.on_event("startup")
async def startup_event():
    print("server started:", datetime.datetime.now())
@app.on_event("shutdown")
async def shutdown_event():
    print("server shutdown:", datetime.datetime.now())
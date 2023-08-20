from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def any_name():
    return {"Message": "Hello kashi fast api developer"}


# to run this script : uvicorn name_of_script:app --reload
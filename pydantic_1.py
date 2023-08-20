import asyncio
from  fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    subjects: List[str] = []

@app.post("/students/")
async def create_student(student: Student):
    return {"student": student}

# testing the api

test_student = {
    "id": 1, 
    "name": "kashi bhattarai",
    "subjects": ["Math", "science"]
    
}

async def test_api():
    response = await create_student(test_student)
    print(response)
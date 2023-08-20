from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

app = FastAPI()
tempplates = Jinja2Templates(directory="templates")
@app.get("/check", response_class=HTMLResponse)
async def hello(request: Request):
    return tempplates.TemplateResponse("hello.html", {"request": request})
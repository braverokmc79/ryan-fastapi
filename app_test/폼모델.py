#   uvicorn 폼모델:app --reload --port 7000 

from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}
    

@app.post("/login/")    
async def login(data:Annotated[FormData, Form()]):
    return {"username": data.username}







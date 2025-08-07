#   uvicorn 폼데이터:app --reload --port 7000 
from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel

app =FastAPI()

class FormData(BaseModel):
    username:str
    password:str
    model_config={"extra":"forbid"}


@app.post("/login/")
async def login(username:Annotated[str, Form()], password:Annotated[str, Form()]):
    return {"username":username}




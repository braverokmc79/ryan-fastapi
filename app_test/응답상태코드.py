#   uvicorn 응답상태코드:app --reload --port 7000 
from turtle import st
from fastapi import FastAPI,status

app = FastAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}






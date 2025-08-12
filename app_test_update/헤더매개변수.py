#   uvicorn 헤더매개변수:app --reload --port 7000 
from typing import List, Union
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token:Union[List[str], None] =Header(default=None)):
    return {"x_token": x_token}

"""
curl -X GET "http://127.0.0.1:7000/items/" \
  -H "X-Token: token1" \
  -H "X-Token: token2" \
  -H "X-Token: token3"

"""
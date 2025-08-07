#   uvicorn HandlingErrors:app --reload --port 7000 
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestler", "bar": "The Bar Wrestler"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


#http://127.0.0.1:7000/items/foo




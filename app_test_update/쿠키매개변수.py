#   uvicorn 쿠키매개변수:app --reload --port 7000 
from typing import Annotated
from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id:Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}



# Test
"""

curl -X GET http://localhost:7000/items/ --cookie "ads_id=abc123"



예: cURL로 테스트
{
  "ads_id": "abc123"
}
"""
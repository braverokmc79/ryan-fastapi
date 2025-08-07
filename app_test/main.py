from enum import Enum
from re import U
from unittest import result
from fastapi import Body, FastAPI, Query
from typing import Annotated, Literal, Union, List ,Set
from pydantic import BaseModel, Field , HttpUrl
from typing_extensions import Annotated, Literal


app = FastAPI()

#본문- 필드

class Image(BaseModel):
    url: HttpUrl
    name: str
    
    
class Item(BaseModel):
    name:str
    description:str | None = Field(
        default=None,
        title="The description of the item",
        max_length=300
    )
    price: float =Field(gt=0, description="The price must be greater than zero")
    tax:List[str] = []
    tags:Set[str]=set()
    images: Union[List[Image], None] = None



@app.put("/items/{item_id}")
async def update_item(item_id: int, item :Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


#Field는 Query, Path와 Body와 같은 방식으로 동작하며, 모두 같은 매개변수들 등을 가집니다.





# class Offer(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price:float
#     items: List[Item] = []
    
    

# @app.post("/offers/")
# async def create_offer(offer:Offer)    :
#     return offer
    
    

# @app.post("/images/multiple/")    
# async def create_multiple_images(images :list[Image]):
#     for image in images:
#         image.url
        
    
    
# @app.get("/index-weights/")
# async def create_index_weights(weights: dict[int, float]):
#     return weights


#Pydantic 모델 속 추가 JSON 스키마 데이터¶
    
# @app.post("/items/{item_id}")
# async def update_item(item_id:int, item: Item)    :
#      results= {"item_id": item_id, "item": item}
#      return results
    
    
    
    

# @app.put("/items/{item_id}")
# async def update_item(item_id:int,item:Annotated[Item,Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results






    
# class FilterParams(BaseModel):
#     model_config = {"extra": "forbid"}

#     limit:int =Field(100, gt=0, le=100)    
#     offset:int = Field(0, ge=0)
#     order_by:Literal["created_at", "updated_at"] = "created_at"
#     tags:list[str] =[]
    
    

# # 쿼리 매개변수 모델
# @app.get("/items/")
# async def read_items(filter_query: Annotated[FilterParams , Query()]):
#     return filter_query





# class ModelName(str, Enum):
#     alexnet= "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
    
    
# class Item(BaseModel):
#     name:str
#     description: Union[str, None] = None
#     price:float
#     tax: float | None = None
    




#쿼리 매개변수와 문자열 검증

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}





# @app.get("/items/")
# async def read_items(
#     q: Union[str, None] = Query(
#         default=None,
#         alias="item-query",
#         title="Query string",
#         description="데이터베이스에서 검색할 항목에 대한 쿼리 문자열(적절한 일치 항목이 있는 경우)",
#         min_length=3,
#         max_length=50,
#         pattern="^fixedquery$",
#         deprecated=True,
#     ),
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results




# @app.get("/items/{item_id}")
# async def read_item(item_id:int):
#     return {"item_id": item_id}



# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name" : model_name, "message": "Deep Learning Model AlexNet"}
    
#     if model_name.value == "lenet":
#         return {"model_name" : model_name, "message": "Deep Learning Model Lenet"}
    
#     return {"model_name" : model_name, "message": "Deep Learning Model ResNet"}





# @app.get("/files/{file_path:path}")
# async def read_file(file_path:str):
#     return {"file_path": file_path}



# #http://127.0.0.1:7000/items2/foo?short=true

# @app.get("/items2/{item_id}")
# async def read_item(item_id:str, q:Union[str, None]=None, short:bool=False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#         print("Query parameter q:", q)
#     if short:
#         item.update({"short": short})
#     return item




# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item




# #http://127.0.0.1:7000/items/foo-item
# @app.get("/items3/{item_id}")
# async def read_user_item(item_id: str, needy:Union[str, None]=None):
#     item = {"item_id": item_id, "needy": needy}
#     return item




# @app.post("/items10/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict


# @app.put("/items10/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}










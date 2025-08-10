#   uvicorn 현재사용자가져오기:app --reload --port 7000 
from typing import Union
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


def fake_decode_token(token):
    return User(
        username=token + "admin",
        email="admin@gmail.com",
        full_name="John Doe",
        password="1111",
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user



@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # 단순 예제용. 실제로는 사용자 검증을 해야 함
    token = form_data.username  # 사용자 이름을 토큰처럼 사용
    return {"access_token": token, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user



"""
curl -H "Authorization: Bearer test123" http://localhost:7000/users/me


"""




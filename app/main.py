from datetime import datetime

from h11 import Response
from pydantic import BaseModel, EmailStr, PositiveInt
from fastapi import FastAPI, File, UploadFile, Cookie

app = FastAPI()


class User(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt
    is_subscribed: bool = False




user_json = """{
    "name":"Ilya",
    "email": "rrr@gmail.com",
    "age": 12,
    "is_subscribed": true
}
"""


users: list[User]=[]
useR=User.parse_raw(user_json)
users.append(useR)


@app.post("/create_user")
def create_user(user: User) -> User:
    users.append(user)
    return user


@app.get("/")
def root(response: Response):
    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")   # получаем текущую дату и время
    response.set_cookie(key="last_visit", value=now)
    return  {"message": "куки установлены"}

# Hello world FastAPI

import uvicorn
from fastapi import FastAPI
import pandas as pd
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    password: str


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


if __name__ == "__main__":
    uvicorn.run("fastapi_auth:app", reload=True)

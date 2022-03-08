from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from pydantic import BaseModel

app = FastAPI()

# may need below for Docker change BASE_DIR
# from pathlib import Path

# BASE_DIR = Path("./").resolve().parent


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    username: str
    email: str
    first_name: str = None
    last_name: str = None
    disabled: bool = None


users = [
    dict(username="bruno", email="bruno@notalk.com", img=True, disable=False),
    dict(username="barb", email="barb@barb.com", img=False, disable=False),
    dict(username="bo", email="bo@bo.com", img=False, disable=True),
]


@app.get("/users/{username}", response_class=HTMLResponse)
async def home(request: Request, username: str):
    """lookup user and send info to webpage"""
    for user in users:
        if username == user["username"]:
            person = user

            if person["disable"] == True:
                return "user not enabled"
    try:
        person  # a match was found
    except NameError:
        raise HTTPException(status_code=404, detail="User not found")

    return templates.TemplateResponse(
        "home.html",
        {"request": request, "usr": person["username"], "img": person["img"]},
    )


if __name__ == "__main__":
    uvicorn.run("fastapi_pred:app", debug=True, reload=True)

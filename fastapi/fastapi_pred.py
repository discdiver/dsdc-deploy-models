from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from pydantic import BaseModel
from loguru import logger

logger.add("file_{time}.log", level="INFO", enqueue=True, rotation="1 month")

app = FastAPI()

# may need below for Docker change BASE_DIR
# from pathlib import Path

# BASE_DIR = Path("./").resolve().parent

# app.mount("/static", StaticFiles(directory=Path(BASE_DIR, "static")), name="static")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    username: str
    email: str
    first_name: str = None
    last_name: str = None
    disabled: bool = None


users = [
    dict(username="bob", email="bob@bob.com", disable=False),
    dict(username="barb", email="barb@barb.com", disable=True),
]


@app.get("/users/{username}", response_class=HTMLResponse)
def home(request: Request, username: str):
    try:
        for user in users:

            if user["username"] == username:
                person = user["username"]
                if user["disable"] == True:
                    return "user not enabled"

                return templates.TemplateResponse(
                    "home.html", {"request": request, "you": user["username"]}
                )
    except Exception:
        logging.log(1, Exception)
    return "Sorry, no such user."


if __name__ == "__main__":
    uvicorn.run("fastapi_pred:app", debug=True, reload=True)

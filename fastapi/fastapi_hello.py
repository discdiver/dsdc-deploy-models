# Hello world FastAPI

import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {"Hello world": "How's it going ?"}


if __name__ == "__main__":
    uvicorn.run("fastapi_hello:app", reload=True, host="0.0.0.0", port=8001)

# Hello world FastAPI

import uvicorn
from fastapi import FastAPI
from datetime import datetime


app = FastAPI()


@app.get("/not-async")
def demo1():
    start = datetime.now()
    vals = dict(zip(range(1_000_00), range(1_000_000)))
    print(f"not-async time: {datetime.now() - start}")
    return vals


@app.get("/yes-async")
async def demo2():
    start = datetime.now()
    vals = dict(zip(range(1_000_00), range(1_000_000)))
    print(f"async time: {datetime.now() - start}")
    return vals


if __name__ == "__main__":
    uvicorn.run("fastapi_async:app", reload=True, host="0.0.0.0", port=8001)

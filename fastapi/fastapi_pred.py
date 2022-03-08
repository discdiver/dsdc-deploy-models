import pickle
import uvicorn
from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import numpy as np

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/form")
async def form(request: Request):
    """form for getting data"""
    return templates.TemplateResponse("form.html", context={"request": request})


@app.post("/form")
async def make_prediction(request: Request):
    """accept form submission and handle it"""

    user_input = request.args

    X_test = np.array(
        [
            int(user_input["OverallQual"]),
            int(user_input["FullBath"]),
            int(user_input["GarageArea"]),
            int(user_input["LotArea"]),
        ]
    ).reshape(1, -1)

    model = pickle.load(open("assets/model.pkl", "rb"))
    pred = model.predict(X_test)
    pred = pred[0]

    return templates.TemplateResponse("results.html", prediction=pred)


if __name__ == "__main__":
    uvicorn.run("fastapi_pred:app", debug=True, reload=True)

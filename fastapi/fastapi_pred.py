import pickle
from urllib import response
import uvicorn
import numpy as np
from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from schemas import FeaturesForm


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/form", response_class=HTMLResponse)
async def features_form(request: Request):
    """form for getting data"""
    return templates.TemplateResponse("form.html", context={"request": request})


@app.post("/form", response_class=HTMLResponse)
async def make_prediction(
    request: Request, user_input: FeaturesForm = Depends(FeaturesForm.as_form)
):
    """accept form submission and make prediction"""

    X_test = np.array(
        [
            int(user_input.OverallQual),
            int(user_input.FullBath),
            int(user_input.GarageArea),
            int(user_input.LotArea),
        ]
    ).reshape(1, -1)

    with open("assets/model.pkl", "rb") as f:
        model = pickle.load(f)

    pred = model.predict(X_test)
    pred = max(0, pred[0])  # ensure no negative predicted values

    return templates.TemplateResponse(
        "results.html", context={"request": request, "prediction": pred}
    )


if __name__ == "__main__":
    uvicorn.run("fastapi_pred:app", debug=True, reload=True)

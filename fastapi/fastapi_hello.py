# Hello world FastAPI

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import plotly.express as px
import plotly

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home():
    return {"Hello world": "How's it going ?"}


@app.get("/not-async")
def demo1():  # async is faster, with even just a few dictionary values 3ms vs 12ms
    return dict(zip(range(1000), range(1000)))


@app.get("/yes-async")
async def demo2():
    return dict(zip(range(1000), range(1000)))


def load_pens() -> pd.DataFrame:
    """load data"""
    df_pens = pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    )
    return df_pens.fillna(-1.01)  # json can't handle NaNs


@app.get("/df")
async def pens_data():
    df_no_nans = load_pens()
    return df_no_nans


# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(content=html_content, status_code=200)


def make_plot(df: pd.DataFrame) -> plotly.graph_objs.Figure:
    """make a plotly plot"""
    fig = px.scatter_3d(
        data_frame=df,
        x="bill_depth_mm",
        y="bill_length_mm",
        z="body_mass_g",
        color="species",
        title="Penguins in 3D!",
    )
    return fig


px_plot = make_plot(load_pens())


@app.get("/plot")
async def plot() -> HTMLResponse:
    """return a plotly plot"""
    return HTMLResponse(px_plot.to_html())
    # fig.to_json() # for deployment in another web framework


if __name__ == "__main__":
    uvicorn.run("fastapi_hello:app", reload=True, host="0.0.0.0", port=8001)

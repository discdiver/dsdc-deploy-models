from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import plotly.express as px
import plotly
import uvicorn
from fastapi import FastAPI
from requests import Request


app = FastAPI()


@app.get("/")
def home():
    return {"Hello world": "Peace"}


templates = Jinja2Templates(directory="templates")


def load_pens() -> pd.DataFrame:
    """load data"""
    df_pens = pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    )
    return df_pens.fillna(-1.01)
    # json can't handle NaNs, creating sentinel value
    # could impute or drop, but this is just for demo purposes


@app.get("/df")
async def pens_data() -> pd.DataFrame:
    """display the data frame"""
    return load_pens()


def make_plot(df: pd.DataFrame) -> plotly.graph_objs.Figure:
    """make a plotly plot and return it"""
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
    """return a plotly plot when queried"""
    return HTMLResponse(px_plot.to_html())
    # fig.to_json() # for deployment in another web framework


if __name__ == "__main__":
    uvicorn.run("fastapi_plot:app", debug=True, reload=True)

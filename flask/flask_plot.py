# Flask with plotly express

import flask
import pandas as pd
import plotly.express as px
import plotly

app = flask.Flask(__name__)


@app.get("/")
def home():
    return "hi"


def load_pens() -> pd.DataFrame:
    """load data"""
    df_pens = pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    )
    return df_pens.fillna(-1.01)  # json can't handle NaNs


@app.get("/df")
async def pens_data():
    return load_pens().to_json()  # can't return a df directly, must turn into json


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
def plot():
    """return a plotly plot"""  # works same as in fastapi
    return px_plot.to_html()
    # fig.to_json() # for deployment in another web framework

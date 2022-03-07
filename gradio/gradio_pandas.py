# gradio_pandas.py

import gradio as gr
import pandas as pd
import plotly.express as px
import codecs
from bs4 import BeautifulSoup


def show_pens(placeholder):
    df_pens = pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    )
    return df_pens  # slow to render a large df


iface = gr.Interface(
    fn=show_pens,
    inputs=["text"],
    outputs=[gr.outputs.Dataframe()],
    description="Table of Palmer Penguins",
    live=True,
).launch(share=True)

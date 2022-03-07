# gradio_plot.py

import gradio as gr
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_pens():
    """plot penguins using matplotlib"""  # plotly doesn't work as of 2.8.7, targeted for 2.9

    df_pens = pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    )
    fig = plt.figure()
    plt.scatter(x=df_pens["bill_length_mm"], y=df_pens["bill_depth_mm"])
    return fig


iface = gr.Interface(
    fn=plot_pens,
    layout="vertical",
    inputs=["checkbox"],
    outputs=["plot"],
    title="Scatterplot of Palmer Penguins",
    description="Let's talk pens. Click to see a plot.",
    article="Talk more about Penguins here, shall we?",
    theme="peach",
    live=True,  # live reloads
).launch(auth=("jeff", "pw"))

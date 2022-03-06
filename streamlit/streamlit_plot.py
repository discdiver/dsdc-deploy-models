# streamlit_plot

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Plotting time")

df_pens = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
)

choice = st.radio("Select color", ["species", "island"])

fig = px.scatter_3d(
    data_frame=df_pens,
    x="bill_depth_mm",
    y="bill_length_mm",
    z="body_mass_g",
    color=choice,
    title="Penguins in 3D!",
)
fig

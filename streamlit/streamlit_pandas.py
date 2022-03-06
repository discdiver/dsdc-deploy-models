# streamlit_pandas.py

import streamlit as st
import pandas as pd

st.title("Streamlit with pandas")

show = st.checkbox("Show dataframe")

df_pens = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
)

if show:
    df_pens

import streamlit as st
from transformers import pipeline

st.header("Story time")

st.image("https://cdn.pixabay.com/photo/2017/07/12/19/03/highway-2497900_960_720.jpg")

col1, col2 = st.columns(2)

with col1:
    input_text = st.text_area("Enter your text here:")
    with st.spinner("Generating story..."):
        generator = pipeline("text-generation", model="gpt2")
        if input_text:
            generated_text = generator(input_text, max_length=60)
            st.success("Here's your story:")
            generated_text[0]["generated_text"]

with col2:
    st.header("I'm in another column")

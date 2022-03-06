# Hello world Gradio 

import gradio as gr

def hello(plane):
    return f"I'm an ultralight {plane} 🛩"

iface = gr.Interface(
    fn=hello,
    inputs=['text'],
    outputs=['text']
).launch()


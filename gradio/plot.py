#delimiter is space
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import codecs
from bs4 import BeautifulSoup
import gradio as gr

def fun2(a,b):
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=list(map(float,a.split(' '))), y=list(map(float,b.split(' ' ))),mode='lines+markers',name='hi',marker=dict(size=10,line=dict(width=2))))

  fig.write_html("test1.html")
  f = codecs.open("test1.html",'r','utf-8')
  doc = BeautifulSoup(f, features='html')
  return str(doc)


gr.Interface(fun2,[gr.inputs.Textbox(default='1 2 3 4'),gr.inputs.Textbox(default='4 2 1 3')],gr.outputs.HTML()).launch()

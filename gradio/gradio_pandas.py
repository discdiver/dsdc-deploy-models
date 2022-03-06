# gradio_pandas.py

import gradio as gr
import pandas as pd
import plotly.express as px
import codecs
from bs4 import BeautifulSoup

def show_pens(alpha):
    df_pens = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
    print(df_pens)
    return df_pens.iloc[:3, :3]
    # scatter_pens = px.scatter_3d(
    #     df_pens, 
    #     x='bill_length_mm', 
    #     y='bill_depth_mm', 
    #     z='flipper_length_mm', 
    #     color='species' 
    #     )
    # scatter_pens.write_json('figscat.html')

    # can't handle plotly, so hacky solution from gradio issue, now fails, tested 

    # with open('figscat.html') as f:
    #     scat = f.read()
    # soup = BeautifulSoup(scat)
    # return soup #df_pens,

    # same as the following
    # f = codecs.open("figscat.html",'r','utf-8')
    # doc = BeautifulSoup(f)
    # return str(doc)

    # with open('plot.html') as f:
    #     html = f.read()
    # call_arg_str = re.findall(r'Plotly\.newPlot\((.*)\)', html[-2**16:])[0]
    # call_args = json.loads(f'[{call_arg_str}]')
    # plotly_json = {'data': call_args[1], 'layout': call_args[2]}    
    # return plotly.io.from_json(json.dumps(plotly_json))


iface = gr.Interface(
    fn=show_pens, 
    inputs=['text'],
    outputs=[gr.outputs.Dataframe()],
    description="Table of Palmer Penguins"
).launch(share=True)
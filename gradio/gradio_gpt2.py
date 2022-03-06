# gradio_gpt2
import gradio as gr

gr.Interface.load(
    "huggingface/gpt2",
    title="Storytelling with GPT2",
    css="""
        body {
            background: rgb(2,0,36);
            background: linear-gradient(180deg, rgba(2,0,36,1) 0%, rgba(7,51,99,1) 70%, rgba(6,3,17,1) 100%); 
        }
        .title {
            color: white !important;
        }
        .article {
            color: white !important;  
            font-size: 1.3em;
        }
        """,
).launch()

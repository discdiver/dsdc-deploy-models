import gradio as gr


def greet(name: str, is_morning: bool, temperature: int) -> tuple[str, str]:
    """give greeting and temperature based on user input

    Args:
        name: user's name
        is_morning: whether it is morning or not

    Returns:
        greeting: a greeting with saluation and temp F
        celsius: temp C
    """

    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees F today"

    celsius = f"It is {round(((temperature - 32) * 5 / 9), 2)} degrees C"
    return greeting, celsius


iface = gr.Interface(
    fn=greet,
    article="Demo",  # p tag under the inputs - anyway to control location?
    inputs=[
        "text",
        "checkbox",
        gr.inputs.Slider(0, 100),
    ],
    outputs=["text", "number"],
    css="""
        body {
            background: rgb(2,0,36);
            background: linear-gradient(180deg, rgba(2,0,36,1) 0%, rgba(7,51,99,1) 70%, rgba(6,3,17,1) 100%); 
        }
        .article {
            color: white !important;  
            font-size: 1.3em;
        }
        """,
).launch(share=True)


# iface.launch(share=True)  #share creates a 72 hour live link
# run with python my_file_name.py

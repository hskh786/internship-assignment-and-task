import gradio as gr
from typer import launch

def square_number(x):
    return x ** 2
gr.Interface(fn=square_number, inputs="number", outputs="number").launch(share=True)
gr.Interface(fn=square_number, inputs="number", outputs="number").launch(share=True)


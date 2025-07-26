import gradio as gr
def reverse_sentence(sentence):
    return sentence[::-1]
interface = gr.Interface(
    fn=reverse_sentence,
    inputs="text",
    outputs="text",
    title="Sentence Reverser",
    description="Enter a sentence and see it reversed!"
)

interface.launch(share=True)    
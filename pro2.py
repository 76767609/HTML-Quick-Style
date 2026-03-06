import gradio as gr

demo = gr.Interface(
    fn=generate_page,
    inputs=[
        gr.Textbox(label="Title"),
        gr.Textbox(label="Text"),
        gr.Dropdown(["blue","green","red","orange"], label="Color")
    ],
    outputs="text",
    title="AI HTML Page Generator"
)

demo.launch()
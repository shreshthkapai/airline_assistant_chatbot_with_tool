import gradio as gr
from main import *

gr.ChatInterface(fn = chat, type = "messages").launch(share = True) 
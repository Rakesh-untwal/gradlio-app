import gradio as gr
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.controllers.chat_controller import ChatController

custom_textbox = gr.MultimodalTextbox(
    file_count="single",
    file_types=['.csv'],
    sources=["upload"],
    interactive=True,
    scale=7,
    placeholder="Upload csv and ask questions"
)

chatController = ChatController()

chat_interface = gr.ChatInterface(
    chatController.chat,
    type= 'messages',
    multimodal=True,
    textbox= custom_textbox,
    title="Csv Quention Answer Tool",
    description="Please upload a csv or ask questions related to data"
)

chat_interface.launch()
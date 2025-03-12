
import gradio as gr
import os

from app.services.csv_service import CsvService
from app.agents.csv_agent import agent
from app.agents.data_visualization_agent import data_visualization_agent
from app.result_types.csv_agent_result_type import CsvDataInvalidQueryResult, CsvDataQueryResult
from app.dependencies.csv_agent_supported_deps import CsvAgentSupportDependencies
from app.dependencies.visulaization_agent_deps import VisualizationAgentDeps
from app.tools.data_visualization_tool import generate_image_path

class ChatController:
    file_path = None

    @classmethod
    def __init__(self):
        print("ChatController initialized")

    @classmethod
    def chat(self,message, history):
        # print(history)
        print(message)
        try:
            image_path = generate_image_path()
            text = message.get("text", "").strip()  # Get text and remove leading/trailing whitespace
            files = message.get("files", [])  # Get files (default to empty list)
            csv_service = CsvService()

            result=None
            if text and files:
                ChatController.file_path = files[0]
                CsvService.upload_csv(files[0])
                if "plot" in text.lower() or "graph" in text.lower():
                    result = data_visualization_agent.run_sync(text,deps = VisualizationAgentDeps(files[0],image_path=image_path))
                    if os.path.exists(image_path):
                        return gr.Image(value=image_path)
                    else:
                        return "Unable to generate the image. Please try again."
                else:
                    result = agent.run_sync(text,deps=CsvAgentSupportDependencies(csv_service= csv_service))
                    print(result.all_messages())
            elif files:
                ChatController.file_path = files[0]
                upload_result = CsvService.upload_csv(files[0])
                return f"{upload_result} How can i assist you to analyze the data. You can ask the questions."
            elif text:
                if ChatController.file_path is None:
                    return "Please upload csv to continue.."
                if "plot" in text.lower() or "graph" in text.lower():
                    result = data_visualization_agent.run_sync(text,deps = VisualizationAgentDeps(ChatController.file_path,image_path=image_path))
                    if os.path.exists(image_path):
                        return gr.Image(value=image_path)
                    else:
                        return "Unable to generate the image. Please try again."
                else:
                    result = agent.run_sync(text,deps=CsvAgentSupportDependencies(csv_service= csv_service))
                    # print(result.all_messages())
            else:
                return "Please ask anything to continue."
            
            print(f"result.data : {result.data}")
            if result is None:
                return "We could not find ans to your question. Please ask the question precisely."
            elif isinstance(result.data,int):
                print(f"Int result : {result.data} ")
                return result.data
            elif isinstance(result.data,str):
                print(f"str result : {result.data} ")
                return result.data
            elif isinstance(result.data,CsvDataQueryResult):
                print(result.data.message)
                return result.data.message
            elif isinstance(result.data,CsvDataInvalidQueryResult):
                print(result.data.message)
                return f"{result.data.message}...{result.data.advice}"
            else:
                print("In the else condition")
                print(result.data.message)
                return result.data.message
        except Exception as e:
            print(f"An error occurred: {e}")
            return f"An error occurred: {e} . Please ask the question accordingly"

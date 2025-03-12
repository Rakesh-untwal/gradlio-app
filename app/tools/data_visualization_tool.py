
from pydantic_ai import RunContext
import pandas as pd
import matplotlib.pyplot as plt
import os
import tempfile
import uuid

from app.dependencies.visulaization_agent_deps import VisualizationAgentDeps

def execute_python_code(ctx: RunContext[VisualizationAgentDeps], code: str) -> str:
    try:
        print("Executing plot code...")
        print(f"Generated Code:\n{code}")

        # Define safe execution environment
        file_path = ctx.deps.image_path
        exec_globals = {"pd": pd, "plt": plt}  # Restrict execution to pandas & matplotlib only
        
        # Ensure a new figure is created before execution
        plt.figure()
        
        # Execute the generated code
        exec(code, exec_globals)

        # Save the figure
        plt.savefig(file_path, bbox_inches="tight")
        plt.close()

        
        print(f"Plot saved at: {file_path}")
        return "The plot has been generated successfully and saved to the specified location."
    except Exception as e:
        print(f"Error in execution: {e}")
        return f"Error executing Python code: {str(e)}. Please correct the code and retry."
    
def generate_image_path():
    """Generate a unique file path for the plot image."""
    return os.path.join(tempfile.gettempdir(), f"plot_{uuid.uuid4().hex}.png")
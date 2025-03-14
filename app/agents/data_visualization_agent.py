
from pydantic_ai import Agent
from pydantic_ai.tools import Tool,RunContext

from app.models.ollama_model import ollama_model
from app.dependencies.visulaization_agent_deps import VisualizationAgentDeps
from app.tools.data_visualization_tool import execute_python_code


data_visualization_agent = Agent(
                                  ollama_model,
                                  system_prompt=(
                                      "You are a data visualization agent that generates **Python code** to create plots based on user queries.\n"
                                      "- You **must use the CSV file provided by the user** at `{csv_path}` to load the data.\n"
                                      "- Ensure the generated code:\n"
                                      "  1. Loads the CSV file using Pandas\n"
                                      "  2. Processes and filters the data as needed\n"
                                      "  3. Creates the requested plot using Matplotlib\n"
                                      "  4. Saves the plot image"
                                  ),
                                  deps_type=VisualizationAgentDeps,
                                  result_retries=5,
                                  tools=[
                                      Tool(execute_python_code)
                                  ],
                                  result_type=str
                        )

# Function to Provide CSV Path to Agent
@data_visualization_agent.system_prompt
def get_csv_path(ctx: RunContext[VisualizationAgentDeps]) -> str:
    return ctx.deps.csv_path  # Pass the CSV file path dynamically
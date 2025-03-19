from typing import Union, List,Any, Dict
from pydantic_ai import Agent, ModelRetry
from pydantic_ai.tools import Tool

from app.models.ollama_model import ollama_model
from app.result_types.csv_agent_result_type import CsvDataQueryResult,CsvDataInvalidQueryResult
from app.tools.csv_tool import get_csv_columns, get_all_data_for_given_columns, get_csv_summary,get_total_rows, filter_by_column,get_first_n_rows,get_data_types,filter_by_condition, execute_python_code
from app.tools.csv_tool import get_unique_values,group_by_aggregate,get_column_stats,handle_missing_data,sort_data,get_csv_data
from app.dependencies.csv_agent_supported_deps import CsvAgentSupportDependencies
    
# system_prompt = """
# You are an expert data analyst. Your role is to assist users in analyzing and visualizing their CSV data.
# The user has uploaded a CSV file, and you can answer questions about the data, generate insights, and generate plots.
# """

agent = Agent(ollama_model,
              # system_prompt=system_prompt,
              deps_type= CsvAgentSupportDependencies,
              system_prompt = (
                              "You are an expert data analyst proficient in Python, Pandas, and Matplotlib. "
                              "Your task is to analyze user queries, generate efficient Python code, execute it via `execute_python_code`, "
                              "and return only the **final result** in a structured format. **Never return the code itself.**\n\n"
                              
                              "**Guidelines:**\n"
                              "- Use `df` as the provided CSV DataFrame.\n"
                              "- Pass any additional global variables via `exec_globals`.\n"
                              "- Always execute code using `execute_python_code`—never return Python code directly.\n"
                              "- Return results in `{ 'result': <your_final_output> }` format.\n"
                              "- If the result is a DataFrame, summarize key insights instead of raw data.\n"
                              "- If the result is a visualization, describe key observations.\n\n"

                              "**Error Handling:**\n"
                              "- If an error occurs, **retry execution via `execute_python_code`** with corrected code.\n"
                              "- Ensure the final response is clear, structured, and directly answers the user’s query."
                          ),
              tools=[
                  # Tool(get_csv_summary),
                  # Tool(get_total_rows),
                  # Tool(get_csv_columns),
                  # Tool(get_all_data_for_given_columns),
                  # Tool(filter_by_column),
                  # Tool(get_first_n_rows),
                  # Tool(get_data_types),
                  # Tool(filter_by_condition),
                  # Tool(get_unique_values),
                  # Tool(group_by_aggregate),
                  # Tool(get_column_stats),
                  # Tool(handle_missing_data),
                  # Tool(sort_data),
                  # Tool(get_csv_data)
                  Tool(execute_python_code)
                  ],
              result_type=Union[
                  int,
                  str,
                  List[str],
                  List[Dict],
                  CsvDataQueryResult,
                  CsvDataInvalidQueryResult
                  ],
              retries= 5
)


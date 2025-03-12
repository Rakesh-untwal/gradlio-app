from typing import Union, List,Any, Dict
from pydantic_ai import Agent, ModelRetry
from pydantic_ai.tools import Tool

from app.models.ollama_model import ollama_model
from app.result_types.csv_agent_result_type import CsvDataQueryResult,CsvDataInvalidQueryResult
from app.tools.csv_tool import get_csv_columns, get_all_data_for_given_columns, get_csv_summary,get_total_rows, filter_by_column,get_first_n_rows,get_data_types,filter_by_condition
from app.tools.csv_tool import get_unique_values,group_by_aggregate,get_column_stats,handle_missing_data,sort_data,get_csv_data
from app.dependencies.csv_agent_supported_deps import CsvAgentSupportDependencies
    
system_prompt = """
You are an expert data analyst. Your role is to assist users in analyzing and visualizing their CSV data.
The user has uploaded a CSV file, and you can answer questions about the data, generate insights, and generate plots.
"""

agent = Agent(ollama_model,
              system_prompt=system_prompt,
              deps_type= CsvAgentSupportDependencies,
            #   model_settings={
            #       "num_ctx": 4096,   # Context window size
            #       "num_threads": 8,  # Number of processing threads
            #       "temperature": 0.2,  # Controls randomness
            #       "top_k": 40,  # Sampling strategy
            #       "num_batch": 4  # Batch processing
            #   },
              tools=[
                  Tool(get_csv_summary),
                  Tool(get_total_rows),
                  Tool(get_csv_columns),
                  Tool(get_all_data_for_given_columns),
                  Tool(filter_by_column),
                  Tool(get_first_n_rows),
                  Tool(get_data_types),
                  Tool(filter_by_condition),
                  Tool(get_unique_values),
                  Tool(group_by_aggregate),
                  Tool(get_column_stats),
                  Tool(handle_missing_data),
                  Tool(sort_data),
                  Tool(get_csv_data)
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


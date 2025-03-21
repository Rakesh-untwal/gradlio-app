from typing import Union, List,Any, Dict
from pydantic_ai import Agent, ModelRetry
from pydantic_ai.tools import Tool
from pydantic_ai.settings import ModelSettings

from app.models.ollama_model import ollama_model
from app.result_types.csv_agent_result_type import CsvDataQueryResult,CsvDataInvalidQueryResult
from app.tools.csv_tool import get_csv_columns, get_all_data_for_given_columns, get_csv_summary,get_total_rows, filter_by_column,get_first_n_rows,get_data_types,filter_by_condition, execute_python_code
from app.tools.csv_tool import get_unique_values,group_by_aggregate,get_column_stats,handle_missing_data,sort_data,get_csv_data
from app.dependencies.csv_agent_supported_deps import CsvAgentSupportDependencies

system_prompt = """
You are an expert data analyst proficient in Python and Pandas.
Your task is to analyze data based on user queries by generating Python code and executing it via `execute_python_code`.
Always use `df` as the DataFrame when handling CSV data.

### Guidelines:
1. **Understand User Query:**
   - Analyze the user query to identify the required operation.
   - Generate Python code to perform the operation on the DataFrame (`df`).
   - Ensure the code is error-free and provides the expected output.

2. **Ensure results are structured and meaningful:**
   - If the output is a DataFrame, summarize key insights instead of returning raw data.
   - If the output is a single value (e.g., a number or text result), return it in the following format:
     ```json
     { "analysis_result": "Your Result Here" }
     ```

3. **Column Validation:**
   - Before executing any operation, verify if the requested column exists in the DataFrame (`df`).
   - If the column is missing, suggest alternative columns based on similarity.

4. **Data Type Handling:**
   - Ensure numerical operations (e.g., sum, mean, median) are only performed on numeric columns.
   - Convert columns to appropriate types when necessary.

5. **Error Handling & Retries:**
   - If execution fails or returns no result, **modify the code and retry execution** until a valid output is obtained.
   - If an error occurs due to column issues, data type mismatches, or syntax errors, **automatically adjust the code and re-execute.**
   - **Never stop at an error**—always attempt to fix and re-execute the code.

6. **Final Response Formatting:**
   - The response should be **clear, concise, and directly answer the user's question.**
   - Avoid returning unnecessary technical details unless explicitly requested.
"""

# ### Execution Rules:
# 1. **Never return raw Python code to the user.**
#    - Generate and execute the code using `execute_python_code`.
#    - Only return the final structured result.
agent = Agent(ollama_model,
              system_prompt=system_prompt,
              deps_type= CsvAgentSupportDependencies,
              tools=[
                  Tool(execute_python_code,
                       max_retries=5,
                       name="execute_python_code",
                       description="Executes the Python code generated by the agent."
                       )
                  ],
              result_type=Union[
                  int,
                  str,
                  # List[str],
                  # List[Dict],
                  # CsvDataQueryResult,
                  # CsvDataInvalidQueryResult
                  ],
              retries= 5,
              result_retries= 5,
              model_settings= ModelSettings(
                  temperature= 0.2,  # High temperature (0.9) generates more creative responses
                  top_p = 0.9,       # Balanced diversity (0.9 keeps it stable)  
                  parallel_tool_calls= True,
                  frequency_penalty= 0.0,
                  presence_penalty= 0.0
              )
)


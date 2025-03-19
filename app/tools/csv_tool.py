from typing import Dict, Any, Callable, List
import pandas as pd
import matplotlib.pyplot as plt
import sys
import io

from pydantic_ai import RunContext, ModelRetry

from app.globals.data import csv_data
from app.dependencies.csv_agent_supported_deps import CsvAgentSupportDependencies

def execute_python_code(ctx: RunContext[CsvAgentSupportDependencies], code: str) -> str:
    try:
        df = pd.read_csv(ctx.deps.csv_path)
        exec_globals = {"pd": pd, "plt": plt, "df": df, "result": None}

        # Capture stdout
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = io.StringIO(), io.StringIO()

        try:
            print(f"Executing Code:\n{code}\n")  # This will be captured
            exec(code, exec_globals)
        finally:
            output = sys.stdout.getvalue().strip()
            error_output = sys.stderr.getvalue().strip()
            sys.stdout, sys.stderr = old_stdout, old_stderr  # Restore original stdout/stderr

        result = exec_globals.get("result", None)

        # If no explicit result, return console output instead
        if result is None:
            return {"analysis_result": output or error_output or "No result or output generated. Please check the code and retry."}
        return {"analysis_result": result}

    except Exception as e:
        print(f"Error during execution: {str(e)}")
        # raise ModelRetry(f"An error occurred: {str(e)}. Please correct the code and retry.")
        raise ModelRetry(f"Error executing Python code:: {str(e)}. Please correct the code and retry.")


def get_csv_columns(ctx: RunContext[CsvAgentSupportDependencies])->list[str] | str:
    return ctx.deps.csv_service.get_csv_columns()

def get_first_n_rows(ctx: RunContext[CsvAgentSupportDependencies],n: int = 5) -> str:
    return ctx.deps.csv_service.get_first_n_rows(n)

def get_data_types(ctx: RunContext[CsvAgentSupportDependencies]) -> Dict[str, str] | str:
    return ctx.deps.csv_service.get_data_types()

def filter_by_condition(ctx: RunContext[CsvAgentSupportDependencies],condition: str) -> str:
    return ctx.deps.csv_service.filter_by_condition(condition)

def get_unique_values(ctx: RunContext[CsvAgentSupportDependencies],column: str) -> list[any] | str:
    return ctx.deps.csv_service.get_unique_values(column)

def group_by_aggregate(ctx: RunContext[CsvAgentSupportDependencies],group_by: str, agg_func: str, column: str) -> str:
    return ctx.deps.csv_service.group_by_aggregate(group_by,agg_func,column)

def get_column_stats(ctx: RunContext[CsvAgentSupportDependencies],column: str) -> Dict[str, float] | str:
    return ctx.deps.csv_service.get_column_stats(column)

def handle_missing_data(ctx: RunContext[CsvAgentSupportDependencies],method: str = "drop", fill_value: Any = None) -> str:
    return ctx.deps.csv_service.handle_missing_data(method,fill_value)
    
def sort_data(ctx: RunContext[CsvAgentSupportDependencies],column: str, ascending: bool = True) -> str:
    return ctx.deps.csv_service.sort_data(column,ascending)

def apply_custom_function(ctx: RunContext[CsvAgentSupportDependencies],column: str, func: Callable) -> str:
   return ctx.deps.csv_service.apply_custom_function(column,func)

def get_csv_data(ctx: RunContext[CsvAgentSupportDependencies]) -> str:
    return ctx.deps.csv_service.export_to_json()

def get_total_rows(ctx: RunContext[CsvAgentSupportDependencies])->int | str:
    return ctx.deps.csv_service.get_total_rows()

def get_all_data_for_given_columns(ctx: RunContext[CsvAgentSupportDependencies],columns:list[str])->str:
    return ctx.deps.csv_service.get_all_data_for_given_columns(columns)

def get_csv_summary(ctx: RunContext[CsvAgentSupportDependencies]) -> str:
    return ctx.deps.csv_service.get_csv_summary()
    
def filter_by_column(ctx: RunContext[CsvAgentSupportDependencies],column: str, value: str) -> str:
   return ctx.deps.csv_service.filter_by_column(column,value)

# def plot_bar_graph(ctx: RunContext[CsvAgentSupportDependencies],x_column: str, y_column: str) -> str:
#     return ctx.deps.csv_service.plot_bar_graph(x_column,y_column)

# def plot_line_chart(ctx: RunContext[CsvAgentSupportDependencies],x_column: str, y_column: str) -> str:
#     return ctx.deps.csv_service.plot_line_chart(x_column,y_column)

# def plot_pie_chart(ctx: RunContext[CsvAgentSupportDependencies],column: str) -> str:
#     return ctx.deps.csv_service.plot_pie_chart(column)


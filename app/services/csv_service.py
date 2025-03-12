import pandas as pd
from typing import Dict, Any, Callable
import app.globals.data

class CsvService:
    csv_data=app.globals.data.csv_data

    @classmethod
    def __init__(self):
        print("Csv Service initialized")

    @staticmethod
    def upload_csv(file):
        # CsvService.csv_data = pd.read_csv(file)
        app.globals.data.csv_data = pd.read_csv(file)
        return "CSV uploaded successfully!"
    
    @classmethod
    def get_csv_columns(self)->list[str] | str:
        try:
            print("get_csv_columns called")
            if app.globals.data.csv_data is not None:
                print(app.globals.data.csv_data.columns.to_list())
                return app.globals.data.csv_data.columns.to_list()
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod
    def get_first_n_rows(self,n: int = 5) -> str:
        print("Get first n rows called")
        try:
            if app.globals.data.csv_data is not None:
                return app.globals.data.csv_data.head(n).to_json(orient="records")
            else:
                return 'Error : Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod
    def get_data_types(self) -> Dict[str, str] | str:
        print("get_data_types called")
        try:
            if app.globals.data.csv_data is not None:
                return app.globals.data.csv_data.dtypes.astype(str).to_dict()
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod
    def filter_by_condition(self,condition: str) -> str:
        try:
            if app.globals.data.csv_data is not None:
                return app.globals.data.csv_data.query(condition).to_json(orient="records")
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod
    def get_unique_values(self,column: str) -> list[any] | str:
        print("Get unique values is called")
        try:
            if app.globals.data.csv_data is not None:
                if column not in app.globals.data.csv_data.columns:
                    return f"Error: Column '{column}' does not exist. Valid columns are: {app.globals.data.csv_data.columns.tolist()}. Please provide a valid column name."
                else :
                    print(app.globals.data.csv_data[column].unique().tolist())
                    return app.globals.data.csv_data[column].unique().tolist()
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod
    def group_by_aggregate(self,group_by: str, agg_func: str, column: str) -> str:
        print("group_by_aggregate is called")
        try:
            if app.globals.data.csv_data is not None:
                if column not in app.globals.data.csv_data.columns:
                    return f"Error: Column '{column}' does not exist. Valid columns are: {app.globals.data.csv_data.columns.tolist()}. Please provide a valid column name."
                else :
                    return app.globals.data.csv_data.groupby(group_by)[column].agg(agg_func).reset_index().to_json(orient="records")
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod
    def get_column_stats(self,column: str) -> Dict[str, float] | str:
        print("get_column_stats is called")
        try:
            if app.globals.data.csv_data is not None:
                if column not in app.globals.data.csv_data.columns:
                    return f"Error: Column '{column}' does not exist. Valid columns are: {app.globals.data.csv_data.columns.tolist()}. Please provide a valid column name."
                else :
                    return {
                            "mean": app.globals.data.csv_data[column].mean(),
                            "median": app.globals.data.csv_data[column].median(),
                            "std": app.globals.data.csv_data[column].std(),
                            "min": app.globals.data.csv_data[column].min(),
                            "max": app.globals.data.csv_data[column].max()
                            }
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod
    def handle_missing_data(self,method: str = "drop", fill_value: Any = None) -> str:
        try:
            if app.globals.data.csv_data is not None:
                if method == "drop":
                    return app.globals.data.csv_data.dropna()
                elif method == "fill":
                    return app.globals.data.csv_data.fillna(fill_value).to_json(orient="records")
                else:
                    return f"Invalid method. Use 'drop' or 'fill'."
            else:
                return 'Error : Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod    
    def sort_data(self,column: str, ascending: bool = True) -> str:
        try:
            if app.globals.data.csv_data is not None:
                if column not in app.globals.data.csv_data.columns:
                    return f"Error: Column '{column}' does not exist. Valid columns are: {app.globals.data.csv_data.columns.tolist()}. Please provide a valid column name."
                else :
                    return app.globals.data.csv_data.sort_values(by=column, ascending=ascending).to_json(orient="records")
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."
    
    @classmethod
    def apply_custom_function(self,column: str, func: Callable) -> str:
        try:
            if app.globals.data.csv_data is not None:
                if column not in app.globals.data.csv_data.columns:
                    return f"Error: Column '{column}' does not exist. Valid columns are: {app.globals.data.csv_data.columns.tolist()}. Please provide a valid column name."
                else :
                    app.globals.data.csv_data[column] = app.globals.data.csv_data[column].apply(func)
                    return app.globals.data.csv_data.to_json(orient="records")
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod
    def export_to_json(self) -> str:
        print(f"Get csv data is called")
        try:
            if app.globals.data.csv_data is not None:
                return app.globals.data.csv_data.to_json(orient="records")
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod
    def export_to_csv(self,file_path: str) -> str:
        try:
            if app.globals.data.csv_data is not None:
                app.globals.data.csv_data.to_csv(file_path, index=False)
                return f"Data exported to {file_path}"
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod
    def get_total_rows(self)->int | str:
        print("Total num of rows called")
        try:
            if app.globals.data.csv_data is not None:
                print(len(app.globals.data.csv_data))
                return len(app.globals.data.csv_data)
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."

    @classmethod
    def get_all_data_for_given_columns(self, columns: list[str]) -> str:
        print(f"get_all_data_for_given_columns called with: {columns}")
        
        try:
            csv_data = app.globals.data.csv_data  # Store reference to avoid multiple lookups
            
            if csv_data is None:
                return 'Error: Please upload a CSV file first.'
            
            missing_columns = [col for col in columns if col not in csv_data.columns]
            if missing_columns:
                return f"Error: The following columns do not exist in the uploaded CSV: {missing_columns}"
            data = csv_data[columns].to_json(orient="records")
            print(f"Here is the resulted data for given columns : {data}")
            return data

        except Exception as e:
            return f"Error: {str(e)}. Please provide valid inputs."

    @classmethod
    def get_csv_summary(self) -> str:
        print(f"Get csv summary is called")
        try:
            if app.globals.data.csv_data is not None:
                print(f"Csv Summart return {app.globals.data.csv_data.describe().to_string()}")
                return app.globals.data.csv_data.describe().to_string()
            else:
                print("CSV is not uploaded")
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."
        
    @classmethod
    def filter_by_column(self,column: str, value: str) -> str:
        try:
            if app.globals.data.csv_data is not None:
                if column not in app.globals.data.csv_data.columns:
                    return f"Error: Column '{column}' does not exist. Valid columns are: {app.globals.data.csv_data.columns.tolist()}. Please provide a valid column name."
                else :
                    return app.globals.data.csv_data[app.globals.data.csv_data[column] == value].to_json(orient="records")
            else:
                return 'Error: Please upload csv first'
        except Exception as e:
            return f"Error: {str(e)} Please provide valid inputs."
        
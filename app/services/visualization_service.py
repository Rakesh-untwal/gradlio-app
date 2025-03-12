import matplotlib.pyplot as plt
import io
import base64
from typing import Dict,Any,List
from app.result_types.data_visualization_result_type import LinePlotColumnName



class VisualizationService:
    @classmethod
    def __init__(self):
        print("Visualization Service initialized")

    @classmethod
    def supported_plot_types(self)->List[str]:
        return ["line","bar","pie"]

    @classmethod
    def get_plot_schema(self,plot_type:str)->Dict[str,Any]:
        print("Get Plot schema called")
        # return LinePlotColumnName
        schemas = {
                "line" : {
                    "x_column_name" : "Column Name",
                    "y_column_name" : "Column Name",
                    "title" : "plot title",
                    "sub_title":"plot sub title"
                }
                # "line": {
                #     "title": "Line Chart",
                #     "xAxis": {
                #         "title": "X-Axis Label",
                #         "values": []
                #     },
                #     "yAxis": {
                #         "title": "Y-Axis Label",
                #         "values": []
                #     },
                #     "series": [
                #         {
                #             "name": "Series 1",
                #             "data": []
                #         }
                #     ]
                # },
                # "bar": {
                #     "title": "Bar Chart",
                #     "xAxis": {
                #         "title": "Categories",
                #         "values": []
                #     },
                #     "yAxis": {
                #         "title": "Values",
                #         "values": []
                #     },
                #     "series": [
                #         {
                #             "name": "Category Series",
                #             "data": []
                #         }
                #     ]
                # },
                # "scatter": {
                #     "title": "Scatter Plot",
                #     "xAxis": {
                #         "title": "X-Axis Label",
                #         "values": []
                #     },
                #     "yAxis": {
                #         "title": "Y-Axis Label",
                #         "values": []
                #     },
                #     "points": [
                #         {"x": 0, "y": 0}
                #     ]
                # }
            }
        return schemas.get(plot_type, {"error": "Invalid plot type"})

    @classmethod
    def draw_line_plot(self,x_data: List[int], y_data: List[int], title: str = "Line Plot") -> str:
        print("Draw line plot is called")
        # Create the plot
        plt.figure()
        plt.plot(x_data, y_data, marker='o')
        plt.title(title)
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        plt.grid(True)

        # Save the plot to a BytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()

        # Encode the image as base64
        buf.seek(0)
        plot_base64 = base64.b64encode(buf.read()).decode('utf-8')
        return plot_base64
    

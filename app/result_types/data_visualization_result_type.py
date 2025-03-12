from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class BasePlotQueryResult(BaseModel):
    title: Optional[str] = None
    xlabel: Optional[str] = None
    ylabel: Optional[str] = None
    grid: Optional[bool] = False
    color: Optional[str] = "blue"

# Schema for Line Chart
class LineChartQueryResult(BasePlotQueryResult):
    message : str = Field(description="Message to user regarding plot insights")
    x_data: List[float]
    y_data: List[float]
    linestyle: Optional[str] = "-"
    marker: Optional[str] = None

class LinePlotSchemaResult(BaseModel):
    title: str = Field(description="Title of plot")
    xAxis: Dict[str,Any] = Field(description="title and x axis values list")
    yAxis: Dict[str,Any] = Field(description= "title and y axis values list")
    series:List[Dict[str,Any]]

# Schema for Bar Graph
class BarGraphQueryResult(BasePlotQueryResult):
    x_data: List[str]
    y_data: List[float]
    bar_width: Optional[float] = 0.8
    align: Optional[str] = "center"

# Schema for Histogram
class HistogramQueryResult(BasePlotQueryResult):
    data: List[float]
    bins: Optional[int] = 10
    range: Optional[tuple] = None
    density: Optional[bool] = False

# Schema for Pie Chart
class PieChartQueryResult(BasePlotQueryResult):
    labels: List[str]
    sizes: List[float]
    explode: Optional[List[float]] = None
    autopct: Optional[str] = "%1.1f%%"
    shadow: Optional[bool] = False

# Schema for Scatter Plot
class ScatterPlotQueryResult(BasePlotQueryResult):
    x_data: List[float]
    y_data: List[float]
    s: Optional[List[float]] = None
    c: Optional[List[str]] = None

class LinePlotResult(BaseModel):
    plot: str = Field(description="Base64-encoded image of the plot")
    description: str = Field(description="Additional description or metadata")

class LinePlotColumnName(BaseModel):
    x_column_name: str = Field(description="Plot x column name")
    y_column_name: str = Field(description="ploy y column name")
    title: str = Field(description="Title of the plot")
    sub_title : str = Field(description="Subtitle of the plot")

class PlotPathResult(BaseModel):
    file_path:str = Field(description="Path of the saved plot")


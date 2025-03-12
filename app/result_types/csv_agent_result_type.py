from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class CsvDataQueryResult(BaseModel):
    message : str | int | float = Field(description="Result message given to user")

class CsvDataInvalidQueryResult(BaseModel):
    message: str = Field(description="Result message given to user")
    advice: str = Field(description="Advice given to user to correct the query")




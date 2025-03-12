from dataclasses import dataclass
from app.services.csv_service import CsvService
from app.services.visualization_service import VisualizationService

@dataclass
class CsvAgentSupportDependencies:
    csv_service : CsvService
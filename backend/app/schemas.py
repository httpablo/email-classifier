from pydantic import BaseModel


class AnalysisResponse(BaseModel):
    original_text: str
    cleaned_text: str
    classification: str
    suggested_response: str
    process_time: float

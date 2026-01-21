from pydantic import BaseModel

class Alert(BaseModel):
    alert_id: str
    type: str
    location: str
    severity: str
    confidence: float

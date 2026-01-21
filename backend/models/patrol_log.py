from pydantic import BaseModel

class PatrolLog(BaseModel):
    zone: str
    start_time: str
    end_time: str

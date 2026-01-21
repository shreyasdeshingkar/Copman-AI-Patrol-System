from pydantic import BaseModel

class Camera(BaseModel):
    camera_id: str
    location: str

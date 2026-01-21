from fastapi import APIRouter

router = APIRouter()

@router.get("/cameras")
def get_cameras():
    return [
        {"camera_id": "CAM_01", "location": "Market Road"},
        {"camera_id": "CAM_02", "location": "Bus Stand"}
    ]

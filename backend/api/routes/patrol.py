from fastapi import APIRouter
from backend.services.summary_service import generate_summary

router = APIRouter()

@router.post("/patrol/summary")
def patrol_summary(payload: dict):
    return generate_summary(payload)

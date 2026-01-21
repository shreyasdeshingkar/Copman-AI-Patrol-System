from fastapi import APIRouter
from backend.services.alert_service import get_active_alerts

router = APIRouter()

@router.get("/alerts")
def fetch_alerts():
    return get_active_alerts()

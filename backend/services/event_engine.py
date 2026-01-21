from backend.config import CROWD_LIMIT

def detect_event(people_count: int):
    if people_count > CROWD_LIMIT:
        return "HIGH_CROWD"
    return None

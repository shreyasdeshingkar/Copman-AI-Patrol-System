def generate_summary(payload):
    zone = payload.get("zone", "Unknown")
    return {
        "zone": zone,
        "summary": (
            f"{zone} experienced moderate crowd movement. "
            "No suspicious behavior detected. "
            "Patrol coverage remained adequate."
        )
    }

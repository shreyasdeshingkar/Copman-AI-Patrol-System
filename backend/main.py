from fastapi import FastAPI
from backend.api.routes import alerts, patrol, cameras

app = FastAPI(title="CopMap AI Patrol System")

app.include_router(alerts.router, prefix="/api")
app.include_router(patrol.router, prefix="/api")
app.include_router(cameras.router, prefix="/api")

@app.get("/")
def health():
    return {"status": "running"}

from fastapi import FastAPI
from app.api.routes import score, goals

app = FastAPI(title="Fintent API")

app.include_router(score.router, prefix="/score")
app.include_router(goals.router, prefix="/goals")
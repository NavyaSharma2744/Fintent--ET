from fastapi import APIRouter
from app.core.goal_agent import process_goals

router = APIRouter()

@router.post("/")
def create_goals(data: dict):
    return process_goals(data.get("text"))
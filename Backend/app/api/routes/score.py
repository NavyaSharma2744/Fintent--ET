from fastapi import APIRouter
from app.core.scoring_engine import calculate_score

router = APIRouter()

@router.post("/")
def get_score(data: dict):
    return calculate_score(data)
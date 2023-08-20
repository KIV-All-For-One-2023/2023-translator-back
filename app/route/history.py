"""
Router for inquiry translation history
"""
from fastapi import APIRouter
from app.service import history
from app.model import schemas

# Create routing method
router = APIRouter()


@router.get("/", response_model=list[schemas.Translate])
async def read_history(skip: int = 0, limit: int = 100):
    """
    Get translation history
    """
    histories = await history.get_history(skip=skip, limit=limit)
    return histories

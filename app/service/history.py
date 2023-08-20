"""
Get translation history
"""
from app.model.mysql import crud


async def get_history(skip: int = 0, limit: int = 100):
    """
    # Get translation history from DB
    """
    return await crud.get_history(skip=skip, limit=limit)

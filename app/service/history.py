from app.model.mysql import crud


async def get_history(skip: int = 0, limit: int = 100):
    return await crud.get_history(skip=skip, limit=limit)

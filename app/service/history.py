from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.model import crud, models, schemas

import requests


async def get_history(db: Session, skip: int = 0, limit: int = 100):
    return await crud.get_history(db=db, skip=skip, limit=limit)

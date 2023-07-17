from fastapi import APIRouter, Path, HTTPException, status, Depends
from app.service import history
from app.model import schemas, models

from sqlalchemy.orm import Session

from app.model.database import MysqlSession, engine
from app.model.models import Base

Base.metadata.create_all(bind=engine)

# Create routing method
router = APIRouter()

# Dependency


def get_db():
    db = MysqlSession()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Translate])
# @router.get("/")
async def read_history(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    histories = await history.get_history(db, skip=skip, limit=limit)
    return histories

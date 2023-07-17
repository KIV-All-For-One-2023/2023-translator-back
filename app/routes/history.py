from fastapi import APIRouter, Path, HTTPException, status, Depends
from app.service import history
from app.model import schemas


# Create routing method
router = APIRouter()

# Query parameter
# https://translate.google.com/?sl=ko&tl=en&text=내 안의 불꽃들로 이 밤을 찬란히 밝히는 걸 지켜봐&op=translate


@router.get("/")
async def get_history(params: schemas.TranslateCreate = Depends()) -> dict:
    mt = await history.translate_text(params)
    return {"translated": mt}
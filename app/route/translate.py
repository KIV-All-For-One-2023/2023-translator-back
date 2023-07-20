"""
Router for translate
"""
from fastapi import APIRouter, Depends
from ..service import translate
from ..model import schemas


# Create routing method
router = APIRouter()

# Query parameter
# https://translate.google.com/?sl=ko&tl=en&text=내 안의 불꽃들로 이 밤을 찬란히 밝히는 걸 지켜봐&op=translate


@router.get("/")
async def translate_text(params: schemas.TranslateCreate = Depends()) -> dict:
    """
    get machine translated text
    """
    mt_text = await translate.translate_text(params)
    return {"translated": mt_text}

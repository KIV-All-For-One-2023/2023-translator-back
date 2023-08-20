from pydantic import BaseModel
from datetime import datetime


class TranslateBase(BaseModel):
    sl: str = "ko"
    tl: str = "en"
    text: str = "내 안의 불꽃들로 이 밤을 찬란히 밝히는 걸 지켜봐"


class Translate(BaseModel):
    id: int
    src_lang: str
    src_text: str
    tgt_lang: str
    mt_text: str
    created_at: datetime

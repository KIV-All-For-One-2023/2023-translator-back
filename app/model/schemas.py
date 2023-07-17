# SQLAlchemy 모델 과 Pydantic 모델models.py 간의 혼동을 피하기 위해 SQLAlchemy 모델이 있는 파일과 schemas.pyPydantic 모델이 있는 파일이 있습니다 .

# 이러한 Pydantic 모델은 "스키마"(유효한 데이터 모양)를 어느 정도 정의합니다.

from pydantic import BaseModel

class TranslateBase(BaseModel):
    sl : str = "ko"
    tl : str = "en"
    text : str = "내 안의 불꽃들로 이 밤을 찬란히 밝히는 걸 지켜봐"
    
class TranslateCreate(TranslateBase):
    mt: str = "Watch me bring the fire and set the night alight"
    
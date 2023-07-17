from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.model import crud, models, schemas

import requests


async def translate_text(params) -> str:
    # MT 모델 서빙 (추후 torchserve 추가 예정.)
    # NMT_URL = f"http://0.0.0.0:8000/predictions/{params.sl}-{params.tl}"

    # """sync post requests"""
    # response = requests.post(NMT_URL, data=params.text.encode("utf8"),
    #                          timeout=5)
    # if response.status_code != 200:
    #     return False
    
    # 아직 MT 모델이 없으므로 기본 리턴 문자열 지정.
    mt = "(mt)Watch me bring the fire and set the night alight"
    setattr(params, 'mt', mt)
    
    # 코드리뷰 요청
    # DB에 저장
    # 번역결과 리턴과 DB 저장을 동시에 하려면? 이미 비동기 적용했으니 상관없나?
    await crud.create_translate(params)

    return mt

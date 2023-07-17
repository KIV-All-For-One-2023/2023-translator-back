from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.model import crud, models, schemas

import requests

import ctranslate2
import sentencepiece as spm


async def translate_text(params) -> str:
    # MT 모델 서빙 (추후 torchserve 추가 예정.)
    # NMT_URL = f"http://0.0.0.0:8000/predictions/{params.sl}-{params.tl}"

    # """sync post requests"""
    # response = requests.post(NMT_URL, data=params.text.encode("utf8"),
    #                          timeout=5)
    # if response.status_code != 200:
    #     return False

    mt = await ctranslate(params)
    setattr(params, 'mt', mt)

    # 코드리뷰 요청
    # DB에 저장
    # 번역결과 리턴과 DB 저장을 동시에 하려면? 이미 비동기 적용했으니 상관없나?
    await crud.create_translate(params)

    return mt


async def ctranslate(params) -> str:

    translator = ctranslate2.Translator(
        f"nmt/model/bin/{params.sl}-{params.tl}", device="cpu")
    sp_sl = spm.SentencePieceProcessor(
        f"nmt/model/sentencepiece/sp_model.{params.sl}")
    sp_tl = spm.SentencePieceProcessor(
        f"nmt/model/sentencepiece/sp_model.{params.tl}")

    input_tokens = sp_sl.encode(params.text, out_type=str)
    results = translator.translate_batch([input_tokens])

    output_tokens = results[0].hypotheses[0]
    output_text = sp_tl.decode(output_tokens)

    return output_text

from sqlalchemy.orm import Session
from sqlalchemy.orm import exc

from fastapi import Depends

from . import models, schemas

from sqlalchemy.orm import Session
from app.model.database import SessionLocal, engine

from app.model import models
models.Base.metadata.create_all(bind=engine)


async def create_translate(translate: schemas.TranslateCreate):
    query = models.Translate(src_lang=translate.sl,
                                    src_text=translate.text,
                                    tgt_lang=translate.tl,
                                    mt_text=translate.mt
                                    )
    try:
        db = SessionLocal()
        db.add(query)
        db.commit()
        db.refresh(query)
    # 기본키에 어긋나는 데이터가 DB에 들어가면 발생
    except exc.IntegrityError:
        raise
    except exc.OperationalError:
        db.rollback()
        raise
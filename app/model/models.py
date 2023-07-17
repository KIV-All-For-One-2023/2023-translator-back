from sqlalchemy import Column, Integer, TEXT, VARCHAR, TIMESTAMP
from sqlalchemy.sql import func
from .database import Base

# ( 위의 파일 ) Base에서 가져옵니다 .databasedatabase.py
# 이를 상속하는 클래스를 만듭니다.
# SQLAlchemy 모델 클래스
class Translate(Base):
    __tablename__ = "translate"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    src_lang = Column(VARCHAR(3), nullable=False)
    src_text = Column(TEXT, nullable=False)
    tgt_lang = Column(VARCHAR(3), nullable=False)
    mt_text = Column(TEXT, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
"""
SQLAlchemy model for MySQL
"""
from sqlalchemy import Column, Integer, TEXT, VARCHAR, TIMESTAMP
from sqlalchemy.sql import func

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Translate(Base):
    """_summary_
    Args:
        Base (_type_): _description_
    """
    __tablename__ = "translate"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    src_lang = Column(VARCHAR(3), nullable=False)
    src_text = Column(TEXT, nullable=False)
    tgt_lang = Column(VARCHAR(3), nullable=False)
    mt_text = Column(TEXT, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=func.now(), onupdate=func.now())

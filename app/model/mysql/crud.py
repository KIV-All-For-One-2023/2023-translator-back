"""
DB CRUD
"""
from sqlalchemy.exc import IntegrityError, OperationalError

from . import MYSQL_SESSION, models

db = MYSQL_SESSION()


async def create_translate(params, mt_text):
    """_summary_
    Create SQLAlchemy model instance and input data
    Args:
        params (_type_): _description_
        mt_text (_type_): _description_
    """
    query = models.Translate(src_lang=params.sl,
                             src_text=params.text,
                             tgt_lang=params.tl,
                             mt_text=mt_text
                             )
    try:
        # db 세션 지정
        db.add(query)
        db.commit()
        db.refresh(query)
    except IntegrityError as error:
        raise ValueError(
            "Error occurs when data that goes against the primary key enters the DB") from error
    # except IntegrityError:
    #     raise
    except OperationalError:
        db.rollback()
        raise
    finally:
        db.close()


async def get_history(skip: int = 0, limit: int = 100):
    """_summary_

    Args:
        skip (int, optional): _description_. Defaults to 0.
        limit (int, optional): _description_. Defaults to 100.

    Returns:
        _type_: _description_
    """
    return db.query(models.Translate).offset(skip).limit(limit).all()

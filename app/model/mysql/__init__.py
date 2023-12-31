"""
Create engine & Session for MySQL
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.model.mysql.models import Base as mysql_base


MYSQL_URL = os.environ.get('SQLALCHEMY_DATABASE_URL')
MYSQL_ENGINE = create_engine(MYSQL_URL)

MYSQL_SESSION = sessionmaker(
    bind=MYSQL_ENGINE, autocommit=False, autoflush=False)

mysql_base.metadata.create_all(bind=MYSQL_ENGINE, checkfirst=True)

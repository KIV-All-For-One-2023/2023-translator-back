from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

MYSQL_URL = os.environ.get('SQLALCHEMY_DATABASE_URL')
engine = create_engine(MYSQL_URL)

MysqlSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
from app.model.database import MysqlSession, engine
from app.model.models import Base as mysql_base
mysql_base.metadata.create_all(bind=engine)
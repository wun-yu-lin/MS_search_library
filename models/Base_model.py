
from sqlalchemy import  BIGINT, TIMESTAMP,create_engine, URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.sql import func
import datetime, sys
sys.path.insert(1, "./")
import config

##  sql config
url_object = URL.create(
    config.DIALECT_DRIVER,
    username=config.MYSQL_USER,
    password=config.MYSQL_PASSWORD, 
    host=config.MYSQL_HOST,
    database=config.MYSQL_DATABASE,
)



class Base(DeclarativeBase):
    type_annotation_map = {
        int: BIGINT,
        datetime.datetime: TIMESTAMP(timezone=True)
    }


class Session_tool():

    def __init__(self):
        self.base = Base
        self.engine = create_engine(url_object)
        self.base.metadata.create_all(self.engine)
        Session =sessionmaker(bind=self.engine)
        self.session = Session()


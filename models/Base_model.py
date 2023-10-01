
from sqlalchemy import create_engine, URL
##資料型別
from sqlalchemy.dialects.mysql import TEXT, DECIMAL, BIGINT, TIMESTAMP, VARCHAR,MEDIUMTEXT, LONGTEXT
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.sql import func
import datetime, sys
sys.path.insert(1, "./")
import config

##  sql config




class Base(DeclarativeBase):
    type_annotation_map = {
        int: BIGINT,
        datetime.datetime: TIMESTAMP(timezone=True),
        float: DECIMAL,
        TEXT: TEXT,
        str: VARCHAR,
        MEDIUMTEXT: MEDIUMTEXT,
        LONGTEXT: LONGTEXT,
        
    }


class SQLALchemy_tool():

    def __init__(self):
        self.url_object = self.create_config_obj()
        self.base = Base()
        self.engine = create_engine(self.url_object)
        self.base.metadata.create_all(self.engine)
        Session =sessionmaker(bind=self.engine)
        self.session = Session()

    def create_config_obj(self):
        url_object = URL.create(
            config.DIALECT_DRIVER,
            username=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD, 
            host=config.MYSQL_HOST,
            database=config.MYSQL_DATABASE,
        )
        return url_object



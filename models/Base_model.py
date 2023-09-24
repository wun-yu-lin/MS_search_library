
from sqlalchemy import  BIGINT, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func
import datetime


class Base(DeclarativeBase):
    type_annotation_map = {
        int: BIGINT,
        datetime.datetime: TIMESTAMP(timezone=True)
    }
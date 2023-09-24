import sys
from typing import Optional
from sqlalchemy import ForeignKey, DateTime, BIGINT, TIMESTAMP
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import datetime

sys.path.insert(1, "./")
from models.table_model import Spectrum_data, Compound_data, Compound_classification


class Spectrum_data_final(Spectrum_data):
    pass
class Compound_data_final(Compound_data):
    pass
class Compound_classification_fianl(Compound_classification):
    pass


spectrum = Spectrum_data_final()
print("done")
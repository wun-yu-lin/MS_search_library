
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import datetime
import sys
sys.path.insert(1, "./")
from models.Base_model import Base


class Spectrum_data(Base):
    __tablename__ = "spectrum_data"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement= True, unique=True,nullable=True)
    ms_level:Mapped[int] = mapped_column(nullable=True)
    compound_data_id:Mapped[int] = mapped_column(ForeignKey('compound_data.id'),nullable=True)
    compound_classification_id:Mapped[int] = mapped_column(ForeignKey('compound_classification.id'),default=None)
    author_id:Mapped[Optional[int]]
    precursor_mz:Mapped[float] = mapped_column(nullable=True)
    collision_energe:Mapped[float] = mapped_column(default=0,nullable=True)
    mz_error:Mapped[float] = mapped_column(nullable=True)
    last_modify:Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())
    date_created:Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())
    data_source:Mapped[str] = mapped_column(String(100), default="unknown",nullable=True)
    tool_type:Mapped[str] = mapped_column(String(100),nullable=True)
    ion_mode:Mapped[str] = mapped_column(String(45),nullable=True)
    ms2_spectrum:Mapped[Optional[str]] = mapped_column(String(65535),nullable=True)






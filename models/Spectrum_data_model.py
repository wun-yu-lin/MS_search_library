
from typing import Optional
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import datetime



##Declare Models
class Base(DeclarativeBase):
    pass

class Spectrum_data(Base):
    __tablename__ = "specturm_data"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement= True, unique=True,nullable=True)
    ms_level:Mapped[int] = mapped_column(nullable=True)
    compound_data_id:Mapped[int] = mapped_column(ForeignKey('compound_data.id'),nullable=True)
    compound_data = relationship("Compound_data", back_populates="specturm_data")
    compound_classification_id:Mapped[int] = mapped_column(ForeignKey('compound_classification.id'),nullable=True)
    compound_classification = relationship("Compound_classification", back_populates="specturm_data")
    author_id:Mapped[Optional[int]]
    precursor_mz:Mapped[float] = mapped_column(nullable=True)
    collision_energe:Mapped[float] = mapped_column(default=0,nullable=True)
    mz_error:Mapped[float] = mapped_column(nullable=True)
    last_modify:Mapped[DateTime] = mapped_column(default=datetime.datetime.utcnow())
    date_created:Mapped[DateTime] = mapped_column(default=datetime.datetime.utcnow())
    data_source:Mapped[str] = mapped_column(String(100), default="unknown",nullable=True)
    tool_type:Mapped[str] = mapped_column(String(100),nullable=True)
    ion_mode:Mapped[str] = mapped_column(String(45),nullable=True)
    ms2_spectrum:Mapped[Optional[list]]










from typing import Any, Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.dialects.mysql import TEXT, DECIMAL, BIGINT, TIMESTAMP, VARCHAR, MEDIUMTEXT, LONGTEXT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import datetime
import sys
sys.path.insert(1, "./")
from models.Base_model import Base

##float to decimal
class Spectrum_data(Base):
    __tablename__ = "spectrum_data"
    ##compound_data_id:Mapped[int] = mapped_column(ForeignKey('compound_data.id'),nullable=True)
    compound_data_id:Mapped[int] = mapped_column(index=True)
    ##compound_classification_id:Mapped[int] = mapped_column(ForeignKey('compound_classification.id'),default=None)
    compound_classification_id:Mapped[int] = mapped_column(index=True)
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement= True, unique=True,nullable=True)
    author_id:Mapped[int]=mapped_column(nullable=True, index=True)
    ms_level:Mapped[int] = mapped_column(nullable=True)
    precursor_mz:Mapped[float] = mapped_column(nullable=True)
    exact_mass:Mapped[float] = mapped_column(nullable=True, index=True)
    collision_energy:Mapped[str] = mapped_column(String(100),default="0",nullable=True)
    mz_error:Mapped[float] = mapped_column(nullable=True)
    last_modify:Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())
    date_created:Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())
    data_source:Mapped[str] = mapped_column(String(100), default="unknown",nullable=True)
    tool_type:Mapped[str] = mapped_column(String(100),nullable=True)
    instrument:Mapped[str] = mapped_column(String(100),nullable=True)
    ion_mode:Mapped[str] = mapped_column(String(45),nullable=True)
    ##ms2_spectrum:Mapped[Optional[str]] = mapped_column(String(5000),nullable=True)
    ms2_spectrum:Mapped[LONGTEXT] = mapped_column(nullable=True)
    precursor_type:Mapped[str] = mapped_column(String(100),nullable=True)

    def __init__(self, ms_level:int, compound_data_id:int, compound_classification_id:int, precursor_mz:float, collision_energy:float, mz_error:float, data_source:str, tool_type:str, ion_mode:str, instrument:str, exact_mass:float, precursor_type:str, ms2_spectrum:str="", author_id:int=0) -> None:
        self.ms_level = ms_level
        self.compound_data_id = compound_data_id
        self.compound_classification_id = compound_classification_id
        self.instrument = instrument
        self.author_id = author_id
        self.precursor_mz = precursor_mz
        self.collision_energy = collision_energy
        self.mz_error = mz_error
        self.data_source = data_source
        self.tool_type = tool_type
        self.ion_mode = ion_mode
        self.exact_mass = exact_mass
        self.precursor_type = precursor_type
        self.ms2_spectrum = ms2_spectrum





        
        






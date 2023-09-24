
from typing import Any, Optional
from sqlalchemy import ForeignKey, BIGINT, TIMESTAMP
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import datetime


##Declare Models
class Base(DeclarativeBase):
    type_annotation_map = {
        int: BIGINT,
        datetime.datetime: TIMESTAMP(timezone=True)
    }

class Spectrum_data(Base):
    __tablename__ = "spectrum_data"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement= True, unique=True,nullable=True)
    ms_level:Mapped[int] = mapped_column(nullable=True)
    compound_data_id:Mapped[int] = mapped_column(ForeignKey('compound_data.id'),nullable=True)
    # compound_data:Mapped["Compound_data"] = relationship(back_populates="spectrum_data")
    compound_classification_id:Mapped[int] = mapped_column(ForeignKey('compound_classification.id'),nullable=True)
    # compound_classification:Mapped["Compound_classification"] = relationship(back_populates="spectrum_data")
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


class Compound_data(Base):
    __tablename__ = "compound_data"
    # spectrum_data:Mapped["Spectrum_data"] = relationship(back_populates="compound_data")
    # compound_classification:Mapped["Compound_classification"] = relationship(back_populates="compound_data")
    compound_classification_id = mapped_column(ForeignKey('compound_classification.id'),nullable=True)
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement= True, unique=True,nullable=True)
    name:Mapped[str] = mapped_column(String(255),nullable=True)
    inchi_key:Mapped[str] = mapped_column(String(255),nullable=True)
    formula:Mapped[str] = mapped_column(String(255),nullable=True)
    smile:Mapped[str] = mapped_column(String(255),nullable=True)
    cas:Mapped[str] = mapped_column(String(255),nullable=True)
    exact_mass:Mapped[float] = mapped_column(nullable=True)
    mole_file:Mapped[str] = mapped_column(String(65535),nullable=True)
    kind:Mapped[str] = mapped_column(String(255),nullable=True)
    pubchem_id:Mapped[str] = mapped_column(String(255),nullable=True, unique=True)
    
##Declare Models

class Compound_classification(Base):
    __tablename__ = "compound_classification"
    # spectrum_data:Mapped["Spectrum_data"]= relationship(back_populates="compound_classification")
    # compound_data:Mapped["Compound_data"] = relationship(back_populates="compound_classification")
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement= True, unique=True,nullable=True)
    classification_kingdom:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_superclass:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_class:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_subclass:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_direct_parent:Mapped[str] = mapped_column(String(255),nullable=True, unique=True)




spectrum_data = Spectrum_data()

# request_data= request.get_json()


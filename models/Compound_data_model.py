
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

class Compound_data(Base):
    __tablename__ = "compound_data"
    spectrum_data = relationship("Spectrum_data", back_populates="compound_data")
    compound_classification = relationship("Compound_classification", back_populates="compound_data")
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
    
    









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

class Compound_classification(Base):
    __tablename__ = "compound_classification"
    spectrum_data = relationship("Spectrum_data", back_populates="compound_classification")
    Compound_data = relationship("Compound_data", back_populates="compound_classification")
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement= True, unique=True,nullable=True)
    classification_kingdom:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_superclass:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_class:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_subclass:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_direct_parent:Mapped[str] = mapped_column(String(255),nullable=True, unique=True)
    









from typing import Any
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import sys
sys.path.insert(1, "./")
from models.Base_model import Base

class Compound_data(Base):
    __tablename__ = "compound_data"
    ##compound_classification_id = mapped_column(ForeignKey('compound_classification.id'),nullable=True)
    compound_classification_id:Mapped[int] = mapped_column(nullable=True)
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement= True, unique=True,nullable=True)
    name:Mapped[str] = mapped_column(String(255),nullable=True)
    inchi_key:Mapped[str] = mapped_column(String(255),nullable=True)
    formula:Mapped[str] = mapped_column(String(255),nullable=True)
    smile:Mapped[str] = mapped_column(String(255),nullable=True)
    cas:Mapped[str] = mapped_column(String(255),nullable=True)
    exact_mass:Mapped[float] = mapped_column(nullable=True)
    mole_file:Mapped[str] = mapped_column(String(5000),nullable=True)
    kind:Mapped[str] = mapped_column(String(255),nullable=True)
    pubchem_id:Mapped[str] = mapped_column(String(255),nullable=True, unique=True)


    def __init__(self,compound_classification_id:int, name:str, inchi_key:str, formula:str, smile:str, cas:str, exact_mass:float, mole_file:str, kind:str, pubchem_id:int)-> None:
        self.compound_classification_id = compound_classification_id
        self.name = name
        self.inchi_key = inchi_key
        self.formula = formula
        self.smile = smile
        self.cas = cas
        self.exact_mass = exact_mass
        self.mole_file = mole_file
        self.kind = kind
        self.pubchem_id = pubchem_id
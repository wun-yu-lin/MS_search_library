
from typing import Any
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.mysql import VARCHAR, TEXT, DECIMAL, MEDIUMTEXT, LONGTEXT
import sys
sys.path.insert(1, "./")
from models.Base_model import Base

class Compound_data(Base):
    __tablename__ = "compound_data"
    ##compound_classification_id = mapped_column(ForeignKey('compound_classification.id'),nullable=True)
    compound_classification_id:Mapped[int] = mapped_column(index=True)
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement= True, unique=True,nullable=True)
    name:Mapped[str] = mapped_column(String(760),nullable=True,default="undefined",index=True)
    inchi_key:Mapped[str] = mapped_column(String(50), index=True,unique=True)
    inchi:Mapped[str] = mapped_column(String(1000),nullable=True)
    formula:Mapped[str] = mapped_column(String(255), index=True)
    smile:Mapped[str] = mapped_column(String(1000),nullable=True)
    cas:Mapped[str] = mapped_column(String(255), index=True, nullable=True)
    exact_mass:Mapped[float] = mapped_column(index=True)
    mole_file:Mapped[LONGTEXT] = mapped_column(nullable=True)
    kind:Mapped[str] = mapped_column(String(255),nullable=True)
    # pubchem_id:Mapped[str] = mapped_column(String(255),nullable=True, unique=True, index=True)


    def __init__(self,compound_classification_id:int, name:str, inchi_key:str,inchi:str, formula:str, smile:str, cas:str, exact_mass:float, mole_file:str, kind:str)-> None:
        self.compound_classification_id = compound_classification_id
        self.name = name
        self.inchi_key = inchi_key
        self.formula = formula
        self.smile = smile
        self.cas = cas
        self.exact_mass = exact_mass
        self.mole_file = mole_file
        self.kind = kind
        # self.pubchem_id = pubchem_id
        self.inchi = inchi
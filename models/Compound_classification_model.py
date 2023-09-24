
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import sys
sys.path.insert(1, "./")
from models.Base_model import Base

class Compound_classification(Base):
    __tablename__ = "compound_classification"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement= True, unique=True,nullable=True)
    classification_kingdom:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_superclass:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_class:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_subclass:Mapped[str] = mapped_column(String(255),nullable=True)
    classification_direct_parent:Mapped[str] = mapped_column(String(255),nullable=True, unique=True)
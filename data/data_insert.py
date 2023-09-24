import sys 
sys.path.insert(1, "./")

from models.Spectrum_data_model import Spectrum_data 
from models.Compound_data_model import Compound_data
from models.Compound_classification_model import Compound_classification

spectrum_data = Spectrum_data()
compound_data = Compound_data()
compound_classification = Compound_classification()
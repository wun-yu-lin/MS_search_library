import sys 
sys.path.insert(1, "./")

from models.Spectrum_data_model import Spectrum_data 
from models.Compound_data_model import Compound_data
from models.Compound_classification_model import Compound_classification

##Session_tool 我自己寫的class
from models.Base_model import Session_tool
session_tool = Session_tool()
session = session_tool.session

def prepare_spectrum_data(monadata_each_object, compound_data_id, compound_classification_id) -> object:
        ##ms_level:int
        ##compound_data_id:int
        ##compound_classification_id:int
        ##precursor_mz:float
        ##collision_energe:float
        ##mz_error:float
        ##data_source:str
        ##tool_type:str
        ##ion_mode:str
        ##mz_error:float
        ##instrument:str
        ##exact_mass:float
        ##precursor_type:str

    data_source = []
    for item in monadata_each_object["tags"]:
        data_source.append(item["text"])
    data_source = str(data_source)



    for item in monadata_each_object["metaData"]:
        item_name = item["name"]
        item_value = item["value"]

        ##ms level
        if item_name == "ms level":
            if item_value == "MS2": ms_level = 2
            if item_value == "MS1": ms_level = 1

        #inonization mode
        if item_name == 'ionization mode':
              if item_value =="positive": ion_mode = "positive"
              if item_value =="negative": ion_mode = "negative"

        ##collision energy
        if item_name == 'collision energy': collision_energe = float(item_value.split(" ")[0])

        ##mz_error
        if item_name == 'mass error': mz_error = float(item_value)

        ##instrument
        if item["name"] == 'instrument': instrument = item["value"]

        ##precursor_mz
        if item_name == 'precursor m/z': precursor_mz = float(item_value)

        ##precursor_type
        if item_name == 'precursor type': precursor_type = item_value
        
        #instrument
        if item_name == 'instrument': instrument = item_value

        #instrument type
        if item_name == 'instrument type': tool_type = item_value

        ##exact mass
        if item_name == 'exact mass': exact_mass = float(item_value)




    spectrum_data = Spectrum_data( 
                ms_level=ms_level,
                compound_data_id=compound_data_id,
                compound_classification_id=compound_classification_id,
                precursor_mz=precursor_mz,
                collision_energe=collision_energe,
                mz_error=mz_error,
                data_source=data_source,
                tool_type=tool_type,
                ion_mode=ion_mode,
                instrument=instrument,
                exact_mass=exact_mass,
                precursor_type=precursor_type
            )
        ##ms_level:int
        ##compound_data_id:int
        ##compound_classification_id:int
        ##precursor_mz:float
        ##collision_energe:float
        ##mz_error:float
        ##data_source:str
        ##tool_type:str
        ##ion_mode:str
        ##mz_error:float
        ##instrument:str
        ##exact_mass:float
        ##precursor_type:str

    
    return spectrum_data


# session_tool = Session_tool()
# session = session_tool.session
# session.add(spectrum_data)
# # session.add(chemical_classification)
# # # session.add(compound_data)
# # session.commit()
# # result = session.query(Spectrum_data).all()
# # for item in result:
# #     print(item)


monadata_each_object = {
    
}
    
import json
#read json in disk mode
with open("./data/test.json", "r") as f:
    monadata_each_object = json.load(f)
    for item in monadata_each_object:
        result = prepare_spectrum_data(item, 1,1)
        session.add(result)
        session.commit()

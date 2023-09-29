import sys,os,time
sys.path.insert(1, "./")

from models.Spectrum_data_model import Spectrum_data 
from models.Compound_data_model import Compound_data
from models.Compound_classification_model import Compound_classification

##Session_tool 我自己寫的class
from models.Base_model import SQLALchemy_tool

sql_alchemy_tool = SQLALchemy_tool()
session = sql_alchemy_tool.session

def prepare_spectrum_data(monadata_each_object, compound_data_id, compound_classification_id) -> object:
    ms_level=None
    precursor_mz=None
    collision_energy=None
    mz_error=None
    data_source=None
    tool_type=None
    ion_mode=None
    instrument=None
    exact_mass=None
    precursor_type=None
    try:
        spectrum_data = None
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
            if item_name == 'collision energy': collision_energy = str(item_value)

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
                    collision_energy=collision_energy,
                    mz_error=mz_error,
                    data_source=data_source,
                    tool_type=tool_type,
                    ion_mode=ion_mode,
                    instrument=instrument,
                    exact_mass=exact_mass,
                    precursor_type=precursor_type,
                    # ms2_spectrum = str(monadata_each_object["spectrum"])
                )
    except Exception as e:
        print(e)
        print("error")
    
    return spectrum_data




results = []
import json
#read json in disk mode
file_url = "./data/MoNA-export-LC-MS-MS_Spectra.json"
##file_url = "./data/test.json"

with open(file_url, "r") as f:
    monadata_each_object = json.load(f)
    for item in monadata_each_object:
        results.append(prepare_spectrum_data(item, 1,1))


for item in results:
    print(item)
    if item == None:
        continue
    try:
        session.add(item)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()



# spectrum_data = Spectrum_data(
#     ms_level=1,
#     compound_data_id=1,
#     compound_classification_id=1,
#     precursor_mz=1,
#     collision_energe=1,
#     mz_error=1,
#     data_source="1",
#     tool_type="1",
#     ion_mode="1",
#     instrument="1",
#     exact_mass=1,
#     precursor_type="1",
#     ms2_spectrum="1"
# )

# session.add(spectrum_data)
# session.commit()
# session.close()

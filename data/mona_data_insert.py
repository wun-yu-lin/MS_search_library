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
                    ms2_spectrum = monadata_each_object["spectrum"]
                )
    except Exception as e:
        print(e)
        print("error")
    
    return spectrum_data

def prepare_compound_data(compound_data_object,compound_classification_id:int=None) -> object:
    name=None
    inchi_key=None
    inchi=None
    formula=None
    smile=None
    cas=None
    exact_mass=None
    mole_file=None
    kind=None
    compound_arr = compound_data_object["compound"]
    if len(compound_arr) > 1:
        print("error")
        print("compound arr length > 1")
    compound_object = compound_arr[0]
    kind = compound_object["kind"]
    mole_file = compound_object["molFile"] 
    
    ##get compound name
    name_arr =[]
    for item in compound_object["names"]:
        name_arr.append(item["name"])
    name = str(name_arr)

    ##get inchey key, formula, smile, cas, exact_mass, pubchem_id
    for item in compound_object["metaData"]:
        item_name = item["name"]
        item_value = item["value"]
        if item_name == "InChIKey": inchi_key = str(item_value)
        if item_name == "InChI": inchi = str(item_value)
        if item_name == "molecular formula": formula = str(item_value)
        if item_name == "SMILES": smile = str(item_value)
        if item_name == "cas": cas = str(item_value)
        if item_name == "total exact mass": exact_mass = float(item_value)

    compound_data = Compound_data(
        compound_classification_id=compound_classification_id,
        name=name,
        inchi_key=inchi_key,
        inchi=inchi,
        formula=formula,
        smile=smile,
        cas=cas,
        exact_mass=exact_mass,
        mole_file=mole_file,
        kind=kind
    )
    return compound_data

def prepare_compound_classification(compound_data_object) -> object:
    classification_kingdom=None
    classification_superclass=None
    classification_class=None
    classification_subclas=None
    classification_direct_parent=None

    ##get classification arr 
    compound_arr = compound_data_object["compound"]
    if len(compound_arr) > 1:
        print("error")
        print("compound arr length > 1")
    
    classification_arr = compound_arr[0]["classification"]

    for item in classification_arr:
        item_name = item["name"]
        item_value = item["value"]
        if item_name == "kingdom": classification_kingdom = str(item_value)
        if item_name == "superclass": classification_superclass = str(item_value)
        if item_name == "class": classification_class = str(item_value)
        if item_name == "subclass": classification_subclas = str(item_value)
        if item_name == "direct parent": classification_direct_parent = str(item_value)

    compound_classification = Compound_classification(
        classification_kingdom=classification_kingdom,
        classification_superclass=classification_superclass,
        classification_class=classification_class,
        classification_subclass=classification_subclas,
        classification_direct_parent=classification_direct_parent
    )
    return compound_classification
    

def insertion_spectrum_data_into_db(file_url:str):
    import json
    #read json in disk mode
    ##file_url = "./data/test.json"
    results = []
    with open(file_url, "r") as f:
        monadata_each_object = json.load(f)
        for item in monadata_each_object:
            results.append(prepare_spectrum_data(item, 1,1))


    for item in results:
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

def insert_compound_classification_into_db(file_url:str):
    import json
    #read json in disk mode
    ##file_url = "./data/test.json"
    results = []
    with open(file_url, "r") as f:
        monadata_each_object = json.load(f)
        for item in monadata_each_object:
            results.append(prepare_compound_classification(item))


        for item in results:
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

def insert_compound_data_into_db(file_url:str):
    import json
    #read json in disk mode
    ##file_url = "./data/test.json"
    results = []
    with open(file_url, "r") as f:
        monadata_each_object = json.load(f)
        for item in monadata_each_object:
            try:
                results.append(prepare_compound_data(item,0))
            except Exception as e:
                print(e)
                continue


        for item in results:
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


def insert_mona_raw_data_into_db(file_url:str):
    '''This function is used to insert mona raw data into db
        currently, we only insert compound_classification, compound_data, spectrum_data table
        table name: compound_classification -> compound_data -> spectrum_data
    '''
    import json
    #read json in disk mode
    ##file_url = "./data/test.json"
    with open(file_url, "r") as f:
        monadata_each_object = json.load(f)
        for item in monadata_each_object:
            spectrum_data = None
            compound_data = None
            current_compound_data_id =0
            compound_classification = None
            current_compound_classification_id =0

            ##嘗試插入compound_classification 進入 database, 如有重複則跳過
            try:
                compound_classification = prepare_compound_classification(item)
                ##直接查詢是否有重複的compound_classification
                compound_classification_query_result =  session.query(Compound_classification).filter(
                        Compound_classification.classification_kingdom == compound_classification.classification_kingdom,
                        Compound_classification.classification_direct_parent == compound_classification.classification_direct_parent
                        ).first()
                ##如果沒有重複的compound_classification, 則插入, 並找到對應的id
                if compound_classification_query_result==None:
                    session.add(compound_classification)
                    session.commit()
                    compound_classification_query_result =  session.query(Compound_classification).filter(
                        Compound_classification.classification_kingdom == compound_classification.classification_kingdom,
                        Compound_classification.classification_direct_parent == compound_classification.classification_direct_parent
                        ).first()
                ##更新對應的id
                current_compound_classification_id = compound_classification_query_result.id
            except Exception as e:
                ##如果有錯誤, 則rollback
                session.rollback()
            finally:
                session.close()

            
            ##取得 compound_classification_id 後, 嘗試插入 compound_data
            try:
                compound_data = prepare_compound_data(item,current_compound_classification_id)
                ##直接查詢是否有重複的compound_data
                compound_data_query_result =  session.query(Compound_data).filter(
                        Compound_data.inchi_key == compound_data.inchi_key
                        ).first()
                ##如果沒有重複的compound data, 則插入, 並找到對應的id
                if compound_data_query_result == None:
                    session.add(compound_data)
                    session.commit()
                    compound_data_query_result =  session.query(Compound_data).filter(
                        Compound_data.inchi_key == compound_data.inchi_key
                        ).first()
                ##更新對應的id
                current_compound_data_id = compound_data_query_result.id
            except Exception as e:

                ##如果有錯誤, 則rollback
                session.rollback()
            finally:
                session.close()

            ##嘗試插入specturm 進入 database
            try:
                spectrum_data = prepare_spectrum_data(
                    monadata_each_object=item,
                    compound_data_id=current_compound_data_id,
                    compound_classification_id=current_compound_classification_id
                )
                session.add(spectrum_data)
                session.commit()
                # print("insertion 1 data complete")

            except Exception as e:
                ##如果有錯誤, 則rollback
                session.rollback()
            finally:
                session.close()

            

    print("total insertion complete, please check database")



    
url = "./data/MoNA-export-LC-MS-MS_Spectra.json"
url = "./data/test.json"
##insertion_spectrum_data_into_db(file_url=url)
##insert_compound_classification_into_db(file_url=url)
##insert_compound_data_into_db(file_url=url)
##result = session.query(Compound_data).filter(Compound_data.id == 10000000).all()

insert_mona_raw_data_into_db(file_url=url)

# #insert files in directory

# import os
# import shutil
# import glob

# directory_path = "./data/splitFile"
# output_directory_path = "./data/output"
# written_files = []


# # 使用 glob 匹配所有 JSON 檔案
# file_paths = glob.glob(os.path.join(directory_path, '*.json'))


# # file_paths = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]
# # file_paths = [os.path.join(directory_path, file) for file in os.listdir(directory_path)]
# # file_paths = [file for file in file_paths if os.path.isfile(file)]
# sorted_file_paths = sorted(file_paths, key=lambda x: os.path.basename(x))

# for file_path in sorted_file_paths:
#     print("Success file: {}".format(file_path))
#     # 假設你的寫入檔案的程式碼在這裡
#     written_files.append(os.path.basename(file_path))
#     try:
#         insert_mona_raw_data_into_db(file_url=file_path)
#         print("Success file: {}".format(file_path))
#     except Exception as e:
#         print("Failed file: {}".format(file_path))
#         continue
#     source_file_path = os.path.join(directory_path, os.path.basename(file_path))
#     destination_directory = os.path.join(output_directory_path, os.path.splitext(os.path.basename(file_path))[0])  # 使用檔案名稱（不含擴展名）作為目標資料夾
#     # 創建目標資料夾
#     os.makedirs(destination_directory, exist_ok=True)
#     # 複製檔案到目標資料夾
#     shutil.copy(source_file_path, destination_directory)

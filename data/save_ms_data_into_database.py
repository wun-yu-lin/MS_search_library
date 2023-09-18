import pymongo 
import sys, os
sys.path.insert(1, "./")
import config
import datetime

monogo_db_config = {
    "url": config.MONGODB_CONFIG_URL,
    "database_name": config.MONGODB_DATABASE_NAME
}


class MongoDB_ms_library_model:
    def __init__(self) -> None:
        try:
            self.mongoDB_connection = pymongo.MongoClient(monogo_db_config["url"])
            self.mongoDB_database = self.mongoDB_connection[monogo_db_config["database_name"]]
            print("connect mongodb success")
        except Exception as err:
            print(err)
            print("connect mongodb error")
    def insert_one_into_ms_data(self, data_object):
        try:
            ##inset one data object into ms_data collection
            self.mongoDB_database["ms_data"].insert_one(data_object)
            print("insert one success")
        except Exception as err:
            print(err)
            print("insert one error")

    def search_many_for_mz_range(self,min_mz, max_mz):
        try:
            ##search data in mz range
            print("start search data")
            start_time = datetime.datetime.now()
            ms_data_collection = self.mongoDB_database["ms_data"]
            cursor = ms_data_collection.find({"mz": {"$gt": min_mz, "$lt": max_mz}})
            end_time = datetime.datetime.now()
            print("End search data")
            print("search data time: ", end_time - start_time)
            search_result = []
            for document in cursor:
                search_result.append(document)

            pass
        except Exception as err:
            print(err)
            print("search data error")

        return search_result



mongoDB_ms_library_model = MongoDB_ms_library_model()

search_results = mongoDB_ms_library_model.search_many_for_mz_range(99,101)

print(search_results)


##create random data arr
# import numpy as np
# arr = np.random.randint(0, 5000, size=2000000)

# dump_json = []

# for item in arr:
#     ##create data object
#     data_object = {
#         "mz": int(item),
#         "intensity": 0.0,
#         "rt": 0.0,
#     }
#     dump_json.append(data_object)

# ##write dump_json to json
# import json
# with open("dump_json.json", "w") as f:
#     json.dump(dump_json, f)
    

        
import os,sys
sys.path.insert(1, "./")
import config
import numpy as np


##split the tree into groups for ms precursor ion
##二元收尋法
class Tree_search:
    def __init__(self, limit_tree_heigh) -> None:
        self.limit_tree_heigh = limit_tree_heigh #int
        self.current_tree_heigh = 0
        self.group_mz_max = 0.0 ##float
        self.group_mz_min = 0.0 ##float 

    def tree_split_group_for_ms_precursor_ion(self, ms1_presursor_ion_mz)->object:
        node_index = 0 
        self.group_mz_max = 5000 ##float
        self.group_mz_min = 0.0 ##float
        self.current_tree_heigh = 0
        split_target_mz = 5000 ## m/z 由 5000開始切
        if ms1_presursor_ion_mz > 5000: return -1 #不處理 mz 5000 以上的數據
        def split_ms_range_group_windows(split_target_mz, node_index):
            if self.current_tree_heigh == self.limit_tree_heigh:
                return {"groupID:": node_index, "group_mz_max": self.group_mz_max,"group_mz_min": self.group_mz_min, "nearest_mz": split_target_mz, "window_size":(self.group_mz_max-self.group_mz_min)}
            self.current_tree_heigh += 1
            ##print("current_tree_heigh", self.current_tree_heigh)

            if (ms1_presursor_ion_mz > split_target_mz):
                self.group_mz_min = split_target_mz
                node_index = node_index*2+2
                return split_ms_range_group_windows(
                        split_target_mz = (self.group_mz_max+self.group_mz_min)*0.5, 
                        node_index=node_index )
            else:
                self.group_mz_max = split_target_mz
                node_index = node_index*2+1
                return split_ms_range_group_windows(
                        split_target_mz = (self.group_mz_max+self.group_mz_min)*0.5, 
                         node_index=node_index )

        return split_ms_range_group_windows(
                    split_target_mz=split_target_mz, 
                    node_index=node_index)
        


 




tree_search = Tree_search(limit_tree_heigh=config.B_TREE_SEARCH_NODE_HEIGH)
search_result = tree_search.tree_split_group_for_ms_precursor_ion(
    ms1_presursor_ion_mz=3122
    )

print(search_result)


## creat a random array about 10000 length
arr = np.random.randint(0, 5000, size=2000000)

##create 

id_map = {}

for item in arr:
    search_result = tree_search.tree_split_group_for_ms_precursor_ion(
    ms1_presursor_ion_mz= item
    )
    if search_result["groupID:"] not in id_map:
        id_map[search_result["groupID:"]] = [1]
    else:
        id_map[search_result["groupID:"]].append(1)
        

##write id_map to json
import json
with open("id_map.json", "w") as f:
    json.dump(id_map, f)

print(id_map)


pass
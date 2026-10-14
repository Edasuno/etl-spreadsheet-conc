import os
import glob
from typing import List
import pandas as pd 

"""
Function for reading raw data and returning a list of DataFrames

Args: input_path (Str): Path folder

return: list: DataFrame List structure
"""

path = "data/input" #Glob Read path

def raw_data_extract(path: str) -> List[pd.DataFrame]:
    total_files = glob.glob(os.path.join(path, "*.xlsx"))

    df_list = []

    for i in total_files:  #Iterate over the dispatched path
        df_list.append(pd.read_excel(i)) 

    return df_list



if __name__ == "__main__":
    df_return_output = raw_data_extract(path)
    print(df_return_output)


import pandas as pd 
from typing import List


"""
Transforming a list of DFs into a single DF



"""

def concatenate_df(data_frame_list: list(pd.DataFrame)) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)
import pandas as pd 
from app.pipeline.transform import concatenate_df
from pandas.testing import assert_frame_equal



"""
Function to test the function used in the transform
"""

def test_concatenate_df():
    
    df1 = pd.DataFrame({"nome": ["Ana", "Bruno"], "idade": [19, 32]})
    df2 = pd.DataFrame({"nome": ["Carlos"], "idade": [33]})

    data_frame_list = [df1, df2]

    expected = pd.DataFrame({
        "nome": ["Ana", "Bruno", "Carlos"],
        "idade": [19, 32, 33],
    })

    # act - Function action with a real result 
    result_test = concatenate_df(data_frame_list)

    # Assert - compare the actual result with the expected. Pandas function
    #Proper way to compare entire Pandas DataFrames
    assert_frame_equal(result_test, expected)

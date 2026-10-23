from pipeline.extract import raw_data_extract
from pipeline.transform import concatenate_df
from pipeline.load import load_dataframe


"""

Main function that executes the entire pipeline 


"""

def main():
    
    path = "data/input"
    df_list = raw_data_extract(path) #Extract

    
    transformed = concatenate_df(df_list) #Transform

    
    load_dataframe(transformed, "data/output/new_sheet.xlsx") #Load

    print("Process complete. All tasks executed successfully")

if __name__ == "__main__":
    main()






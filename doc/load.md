# Export Dataframe as a .xlsx

## Function action

My Function `load_dataframe` exports a Pandas DataFrame to an Excel file (.xlsx). If the parent directories in the target path do not exist, the function automatically creates them before saving the file, omitting the DataFrame index by default.



## input 
- data_frame (pd.DataFrame): The DataFrame object containing the structured data to be written to the Excel file.

- output_path (str): absolute or relative string path (including the file name and .xlsx extension) where the Excel file should be saved.

## Output

`None`: The function performs an I/O disk operation and returns no value (None).

Despite generating and creating the 'output' folder the function's return value is empty.



## Operational dependencies
`pandas`: Primary library used to manage the tabular dataset and provide the to_excel export method.

`pathlib.Path`: Standard Python library module used for cross-platform, object-oriented path manipulations.

`openpyxl` : Required under the hood by Pandas to write `.xlsx` file. Ensure it is installed in your environment.

## Usage

Import the function into the main file.

Pass the variable containing the transformed dataframe as an argument, followed by the absolute or relative path (str) to the desired output location.


## Notes

This project involves concatenating several tables into a single one, which is why 'load.py' doesn't connect to a database.




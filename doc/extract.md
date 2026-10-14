# Raw Data Extraction

## Function action

My Function `raw_data_extract()` function reads Excel files from a specified directory and returns their contents as a list of pandas DataFrames.

The function specifies the path for the Glob library to search for all .xlsx files.

An empty list is created and a for loop iterates over the path and adds items to the list using the `append` method.

Using the iterated spreadsheets as arguments for the pandas `pd.read_excel` method.

Finally returning to the now-complete list.

## Input

- `path` (str): Path to the directory raw data containing the .xlsx files. Where the raw data is located.


## Output

- `list[pd.DataFrame]`: A list containing one DataFrame for each Excel file found.

## Operational dependencies

- `pandas`
- `openpyxl`

Run the command :
````
poetry install
````

## Usage

Import the function into the main file.

The variable receives the function with the path argument.

```python
from app.pipeline.extract import raw_data_extract

df_list = raw_data_extract("data/input")
```

## Notes

- Only `.xlsx` files are included.
- The function returns an empty list if no matching files are found.
- The relative path is interpreted from the current working directory.

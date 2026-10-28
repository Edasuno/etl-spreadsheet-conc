# Dataframe Concatenation

This function merges multiple Pandas DataFrame objects from a list into a single and unified DataFrame, resetting the row index to ensure a clean and continuous sequence.

## Input 

`data_frame_list (list[pd.DataFrame])` is a list containing the individual Pandas DataFrames that you want to combine.

## Output

Your new dataframe after `pd.DataFrame` is a new combined DataFrame resulting from the vertical concatenation of all input tables.

## Operational dependencies

`pandas`: Core library used for data manipulation and the concat operation.

`typing.List`: Python typing module used for type hint input parameters.


## Usage
It takes a list of DataFrames as an argument, applies the concatenation function, and returns the resulting DataFrame ready for use.

## Notes

The `typing` module serves to identify a data type as `list` for future use.

`ignore_index=True` is crucial because it discards the original overlapping indices from each separate table and generates a new continuous integer index.
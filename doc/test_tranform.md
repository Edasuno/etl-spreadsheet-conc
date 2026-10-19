# Transform test

## Function action

My Function `def test_concatenate_df()` refers to an automated test of the [AAA](https://semaphore.io/blog/aaa-pattern-test-automation) type. It uses two pre-created dataframes as the main scenario for the test.

Placing them as an array of dataframes. It also shows the expected result and using the `assert_frame_equal` function from the `pandas.testing` module, it compares the result against the expected outcome.

## Operational dependencies

- `pandas`
- `pytest`

## Usage

Run your test : 
```
poetry run pytest tests/test_pipeline.py -v
```

## Notes

- assert_frame_equal() is used to compare entire Pandas DataFrames, including their values, index, columns, and data types.

- The test validates the expected concatenation of multiple DataFrames into a single DataFrame.




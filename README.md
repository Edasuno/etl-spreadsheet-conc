# Extract, Transform, and Load (ETL) focused on working with Excel spreadsheets

## Introduction

The project goal is to receive multiple spreadsheets from various sources and concatenate them into a single file using data manipulation operations.

The most important aspect is that the project itself is a custom initiative, designed to improve project organization and make it more readable for other professionals, using folder modularization and a better project architecture.

The raw input data files should be placed in the "data/input" folder, while the output will be generated in a folder named "output" (located in the same directory).

The specific filenames don't matter, as the process will automatically detect and include any file with an `.xlsx` extension.

## Dependencies

### Using Pyenv

This project uses pyenv to manage Python versions.

[Check pyenv githug page.](https://github.com/pyenv/pyenv)

---

### Using Poetry (Recommended):

This project uses Poetry for dependency management and packaging. 


1. Install Poetry (if you haven't already)

```
curl -sSL https://install.python-poetry.org | python3 -

```
2. install dependencies

Navigate to the project root directory and run the install command to automatically download and configure everything defined in `pyproject.toml`.


```
poetry install
```

This project use : 

- pandas
- openpyxl
- pytest
- pathlib
- glob



## How to run this ETL project

To run this project :

1. Clone this repository
2. Set the Python version using `pyenv local 3.14`
3. Ensure the necessary dependencies are already installed by using the command from the previous session.
4. Run the scripts `poetry run python app/main.py`
5. Check the output of the functions


## Conclusion

This project was built as a personal challenge to elevate my standards of code organization, modularity, and architectural design.

As developer i know that poorly structured code creates unnecessary friction and wastes valuable time during code reviews and maintenance. On the other hands, a well organized and thoroughly documented project provides instant clarity making it significantly easier to navigate, scale, and collaborate on, whether working solo or with a others. 

Upon finishing this project, I realized how much I’ve improved in documentation, type hinting (even in a dynamically typed language), and gaining a much stronger sense of control over every part of the code.




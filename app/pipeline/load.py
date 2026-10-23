import pandas as pd
from pathlib import Path

"""

Export a DataFrame to an Excel file.

"""

def load_dataframe(data_frame: pd.DataFrame, output_path: str) -> None:

    path = Path(output_path)

    path.parent.mkdir(parents=True, exist_ok=True)

    data_frame.to_excel(path, index=False)


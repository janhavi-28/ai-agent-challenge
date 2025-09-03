
import pandas as pd

def parse(pdf_path: str) -> pd.DataFrame:
    # TODO: Replace with actual PDF parsing logic
    df = pd.read_csv(r"data\sbi\sbi_sample.csv")
    return df

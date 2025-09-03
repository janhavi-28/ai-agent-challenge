import pandas as pd
from custom_parsers.icici_parser import parse

def test_icici_parser():
    expected = pd.read_csv("data/icici/icici_sample.csv")
    actual = parse("data/icici/icici_sample.pdf")
    assert expected.equals(actual)

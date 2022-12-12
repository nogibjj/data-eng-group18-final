"""Test that query logics in the main file works"""

import pandas as pd

df = pd.read_csv("cost_of_living.csv")


def test_df_ingestion():
    """Test that dataframe was properly ingested"""
    assert (df.shape[0] == 4956) & (df.shape[1] == 58)

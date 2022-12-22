"""Test that query logics in the main file works"""

import pandas as pd

df = pd.read_csv("cost_of_living.csv")


def test_df_ingestion():
    """Test that dataframe was properly ingested"""
    assert (df.shape[0] == 4956) & (df.shape[1] == 58)


"""API Testing"""


from fastapi import FastAPI
import httpx
from fastapi.testclient import TestClient
from .main import app


@app.get("/test")
async def test_read_main():
    return {"msg": "Test message"}

client = TestClient(app)


def test_read_main():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"msg": "Test message"}

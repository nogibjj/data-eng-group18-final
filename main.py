"""FastAPI application for querying global cost of living dataset"""

from fastapi import FastAPI
import uvicorn
import pandas as pd

# Initiate the FastAPI app
app = FastAPI()

df = pd.read_csv("cost_of_living_cleaned.csv")

def cost_of_living(city, country): 
    



@app.get("/")
async def root():
    """Define Root Path"""
    return {
        "Welcome!": "Use this API application to get updated cost-of-living data in over 4500 cities globally."
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

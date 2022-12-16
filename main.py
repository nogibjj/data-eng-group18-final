"""FastAPI application for querying global cost of living dataset"""

from fastapi import FastAPI
import uvicorn
import pandas as pd

# Initiate the FastAPI app
app = FastAPI()

df = pd.read_csv("cost_of_living_cleaned.csv")


@app.get("/")
async def root():
    """Define Root Path"""
    return {
        "Welcome!": "Use this API application to get updated cost-of-living data in almost 5,000 cities globally."
    }


@app.get("/cost_of_living/{city}/{country}")
async def your_location_specific(city: str, country: str):
    """Return cost of living estimates given a city and country"""
    if (city not in df["city"].unique()) | (country not in df["country"].unique()):
        return {"Error": "The city you are looking for is not in our database."}
    # Filter the dataframe for the specific city and country
    city_specific_df = df.loc[(df["country"] == country) & (df["city"] == city)]
    # Get the higher and lower cost of living
    higher = float(city_specific_df["higher_cost_of_living"])
    lower = float(city_specific_df["lower_cost_of_living"])
    return_message = f"The cost of living for {city}, {country}, can range from ${lower} to ${higher} in USD."
    return {"Result": return_message}


@app.get("/cuppacino_cost/{city}/{country}")
async def cuppacino_cost(city: str, country: str):
    """Return cost estimates of a cup of cuppacino given a city and country"""
    if (city not in df["city"].unique()) | (country not in df["country"].unique()):
        return {"Error": "The city you are looking for is not in our database."}
    # Filter the dataframe for the specific city and country
    city_specific_df = df.loc[(df["country"] == country) & (df["city"] == city)]
    # Get the cuppacino cost
    cost = float(city_specific_df["cappuccino_restaurant"])
    return {
        "Result": f"A cup of cappuccino costs around ${cost} USD in {city}, {country}."
    }


@app.get("/milk_cost/{city}/{country}")
async def milk_cost(city: str, country: str):
    """Return cost estimates of milk given a city and country"""
    if (city not in df["city"].unique()) | (country not in df["country"].unique()):
        return {"Error": "The city you are looking for is not in our database."}
    # Filter the dataframe for the specific city and country
    city_specific_df = df.loc[(df["country"] == country) & (df["city"] == city)]
    # Get the milk cost
    cost = float(city_specific_df["milk"])
    return {"Result": f"A liter of milk costs around ${cost} USD in {city}, {country}."}


@app.get("/gas_cost/{city}/{country}")
async def gas_cost(city: str, country: str):
    """Return cost estimates of milk given a city and country"""
    if (city not in df["city"].unique()) | (country not in df["country"].unique()):
        return {"Error": "The city you are looking for is not in our database."}
    # Filter the dataframe for the specific city and country
    city_specific_df = df.loc[(df["country"] == country) & (df["city"] == city)]
    # Get the gasoline cost
    cost = float(city_specific_df["gasoline"])
    return {
        "Result": f"A liter of gasoline costs around ${cost} USD in {city}, {country}."
    }


@app.get("/apartment_downtown_cost/{city}/{country}")
async def apartment_downtown_cost(city: str, country: str):
    """Return cost estimates of milk given a city and country"""
    if (city not in df["city"].unique()) | (country not in df["country"].unique()):
        return {"Error": "The city you are looking for is not in our database."}
    # Filter the dataframe for the specific city and country
    city_specific_df = df.loc[(df["country"] == country) & (df["city"] == city)]
    # Get the gasoline cost
    cost = float(city_specific_df["one_bdrm_apt_downtown"])
    return {
        "Result": f"A one-bedroom apartment downtown costs around ${cost} USD in {city}, {country}."
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

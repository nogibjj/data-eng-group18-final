"""FastAPI application for querying global cost of living dataset"""

from fastapi import FastAPI
import uvicorn
import pandas as pd
import json

# Initiate the FastAPI app
app = FastAPI()

df = pd.read_csv("cost_of_living_cleaned.csv")

def cost_of_living(city, country): 
    country_df = df[df['country'] == country]
    city_df = country_df[country_df['city'] == city]

    higher = city_df['higher_cost_of_living']
    higher = higher.astype(str)
    higher = higher.tolist()
    higher = higher[0]

    lower = city_df['lower_cost_of_living']
    lower = lower.astype(str)
    lower = lower.tolist()
    lower = lower[0]
    higher_and_lower = higher + "," + lower
    #parsed = json.loads(higher_and_lower)
    #json.dumps(parsed, indent=4)  
    #return parsed
    return higher_and_lower



@app.get("/")
async def root():
    """Define Root Path"""
    return {
        "Welcome!": "Use this API application to get updated cost-of-living data in over 4500 cities globally."
    }


@app.get("/col/{city}/{country}")
def your_location_specific(city: str, country: str):
    to_user = cost_of_living(city, country)
    higher, lower = to_user.split()
    return_message = f"The higher cost of living for {city}, {country}, is {higher}, and the lower cost of living is {lower} in USD."
    return_dict = {"Result" : return_message}
    parsed = json.loads(return_dict)
    json.dumps(parsed, indent=4)  
    return parsed
    #return return_dict

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

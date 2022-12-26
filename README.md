# Cost of Living Calculator

![Continuous Integration with Github Actions](https://github.com/nogibjj/data-eng-group18-final/actions/workflows/main.yml/badge.svg)

This project aims to use FastAPI's Swagger UI documentation system to help users look up cost of living incidices in cities across the globe. 

## Project Diagram

![final_diagram](https://user-images.githubusercontent.com/60377132/208192868-9116d6cb-de85-4a82-8357-7e75cd645c24.png)

## Data Source

The dataset we utilized for this project was the "Global Cost of Living" dataset in [Kaggle](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living), which was gathered by scraping the Numbeo cost of living database. The dataset contains information on various common consumer goods, such as the price of one dozen eggs, as well as standard living expenses, such as the price to rent a one-bedroom apartment in the city center. 

## Cost of Living Calculation

To determine our the range of cost of living for a given city, we generate a "higher" estimate and a "lower" estimate, corresponding to what a person with more income and what a person with less income might spend per month to live. The higher cost of living contains more nonessential expenses, such as more occasions dining out and an apartment downtown instead of the suburbs. 

Here is the full breakdown of what indices we used to calculate each estimate:

* Higher estimate for Cost of Living: 4 Inexpensive Meals + 2 McDonald McMeals + 3 Domestic Beer (at restaurant) + 8 Cappucinos (at restaurant) + 6 Water (at restaurant) + 5kg white rice + 2 dozen eggs + 2kg local cheese + 4kg chicken fillets + 2kg beef + 1kg apples + 1kg oranges + 1kg tomato + 1kg potato + 1kg onion + 3 heads lettuce + 2 bottles wine + 1 domestic beer (market) + 1 monthly metro pass + 2 taxi rides (1km each) + basic utilities + internet cost + 1 fitness club pass + 2 movie tickets + 1 one-bedroom downtown apartment

* Lower estimate for Cost of Living: 6 McDonald McMeals + 4 Cappucinos (at restaurant) + 6 Water (at restaurant) + 5kg white rice + 2 dozen eggs + 2kg local cheese + 4kg chicken fillets + 2kg beef + 1kg apples + 1kg oranges + 1kg tomato + 1kg potato + 1kg onion + 3 heads lettuce + 2 domestic beer (market) + 1 monthly metro pass + 2 taxi rides (1km each) + basic utilities + internet + 1 fitness club pass + 2 movie tickets + 1 one-bedroom suburban apartment

Based on these standard costs of living, the user is able to ask our app what the range of cost of living is for any city in our database. The user can also ask for the cost of individual goods in a city, including a cup of cuppacino or gallon of gas. 

## Replicating the project

Users can run the FastAPI app by cloning the repository, installing the required softwares and running the script containing the application as such:

```
make install
python main.py
```

You can also run the docker image we created and pushed to the hub by running this line of code:

```
docker run -p 8080:8080 genesisqu/cost-of-living-calculator:lastest
```

## Testing

Testing was conducted on API Endpoints using FastAPI's TestClient object using the httpx library and Starlette ASGI framework/ toolkit. Starlette allows for pytest (with is utilized in our GitHub Action's CI/CD) to be used directly with FastAPI. All testing is contained in the test_main.py file. 

## CI/CD

This project is connected to AWS, using Codebuild and AppRunner. 

<img width="1440" alt="Screenshot 2022-12-26 at 1 28 59 AM" src="https://user-images.githubusercontent.com/110945807/209512122-38d4f4fd-79e9-4a01-90e3-1e86c5e081c3.png">
<img width="1440" alt="Screenshot 2022-12-26 at 1 29 34 AM" src="https://user-images.githubusercontent.com/110945807/209512127-091c901a-2b10-4d9f-a70e-d5bd4608ad6c.png">

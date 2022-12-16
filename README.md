# Cost of Living Lookup

![Continuous Integration with Github Actions](https://github.com/nogibjj/data-eng-group18-final/actions/workflows/main.yml/badge.svg)

This project aims to use FastAPI's Swagger UI documentation system to help users look up cost of living incidices in cities across the globe. 

The dataset we utilized for this project was the "Global Cost of Living" dataset in Kaggle (https://www.kaggle.com/datasets/mvieira101/global-cost-of-living), which was gathered by scraping the Numbeo cost of living database. The dataset contains information on various common consumer goods, such as the price of one dozen eggs, as well as standard living expenses, such as the price to rent a one-bedroom apartment in the city center. 

To determine our "lower" and "higher" costs of living, we estimated what a person with more income versus a person with less income might spend per month to live. The higher cost of living contains more nonessential expenses, such as more occasions dining out and an apartment downtown instead of the suburbs. 

Based on these standard costs of living, the user is able to ask our app what the range of cost of living is for any city in our database. The user can also ask for the cost of individual goods in a city, including a cup of cuppacino or gallon of gas. 
# Machine Learning, Analyzing SpaceX Falcon 9 Launch Data

## Introduction 
SpaceX advertises Falcon9 rocket launches with a cost of 62 million dollars where other providers cost upwards of 165 million dollars each, mostly because SpaceX can reuse the first stage. But there are times where the first stage does not land, or it will crash mid-flight, or even being sacrificed due to various mission parameters. In this project, we will determine the price of each launch by gathering information and training a machine learning model to predict if SpaceX will be able to reuse the first stage. 

## Overview
The goal of this project is to identify the different factors that influence the success rate of SpaceX Falcon9 rocket landing.

## Tools and Programming Language(s)
Jupyter Notebook, Python, SQL, Plotly

## Process
1. Obtain data through web-scraping (BeautifulSoup) and RESTAPI (SpaceX website).
2. Perform data cleaning and data wrangling to investigate the interested variables. 
3. Conduct in-depth EDA and build visualizations to better understand the data.
4. Build an interactive visual analytics to study the geospatial variables and the success rate of the launchings.
5. Peform predictive classification analysis with multiple machine learning algorithms, which include logistic regression, support vector machine, decision tree classifier and K nearest neighbours.
6. Compare the performance for all models and choose a model with the highest accuracy score.

## Results
Decision Tree Classifier has the highest accuracy score of 90.18%. 



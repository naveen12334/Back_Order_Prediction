# Back_Order_Prediction
Predicting whether the product will be gone in Back Order or not.

# Input Values
![](https://github.com/naveen12334/Back_Order_Prediction/blob/main/Before.PNG)

# Result
![](https://github.com/naveen12334/Back_Order_Prediction/blob/main/After.PNG)

# Problem Statement:
Backorders are unavoidable, but by anticipating which things will be backordered, 
planning can be streamlined at several levels, preventing unexpected strain on 
production, logistics, and transportation. ERP systems generate a lot of data (mainly 
structured) and also contain a lot of historical data; if this data can be properly utilized, a 
predictive model to forecast backorders and plan accordingly can be constructed. 
Based on past data from inventories, supply chain, and sales, classify the products as 
going into backorder (Yes or No).

# Goal:
The main Goal is to predict the back order of the products based on different factors available in the provided dataset.

# Approach:
The classical machine learning tasks like Data Exploration, Data Cleaning, 
Feature Engineering, Model Building and Model Testing. Try out different machine 
learning algorithms that’s best fit for the above case.

# Dataset:
https://github.com/rodrigosantis1/backorder_prediction/blob/master/dataset.rar

# Project Various Steps:
# Data Exploration
I started exploring datasets using pandas, NumPy,matplotlib and seaborn.


# Data visualization
Ploted colleration matrix to get insights about dependend and independed variables. Made chats like( Bocxplot,countplot,distplot,pairplot).

# Model Selection
Made many Models But selected LIGHT GBM Classifier.

# Hyperparameter Optimization
Using Randomizedsearch CV and GridSearch CV to select the best parameter for training the model

# Model Dump
As per selected trained model is dumped to pickled format for app development

# Model Accuracy 
92%

# Deployed:
https://backorderpre.herokuapp.com/

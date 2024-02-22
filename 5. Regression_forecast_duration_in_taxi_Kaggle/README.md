# 5. Regression Task, Taxi Trip Duration Prediction for Kaggle

## Table of Contents  
1. Project Description
2. Problem Statement
3. Brief Data Overview
4. Project Workflow
5. Results 
6. Conclusions

### Project Description    
  
The machine learning task is aimed at automating business processes. The goal is to build a model that predicts the total duration of taxi trips in New York.

Trip duration depends on many factors such as the starting and ending point of the trip, the time of day, weather conditions, and so on. Thus, it is necessary to develop an algorithm capable of determining the duration of the trip and forecasting its cost in the most trivial way, for example, by simply multiplying the cost by a given tariff. Taxi services store vast amounts of information about trips, including data such as the final and initial route points, trip date, and its duration. This data can be used to predict trip duration automatically using artificial intelligence.

### Problem Statement    

Build a machine learning model that, based on the provided client characteristics, will predict a numerical feature - taxi trip duration. In other words, solve a regression task.

**Competition Conditions:**  
It is necessary to identify characteristics and, using them, predict the duration of taxi trips.

**Quality Metric**     
RMSLE

**Practiced Techniques**     
Feature engineering, machine learning methods, model selection

### Brief Data Overview
Kaggle competition data:
https://www.kaggle.com/competitions/nyc-taxi-trip-duration/discussion/39553

### Project Workflow  
1. Form a dataset based on multiple information sources
2. Design new features using Feature Engineering and identify the most significant ones when building the model
3. Explore the provided data and identify patterns
4. Build multiple models and select the best one based on the specified metric
5. Design the process of predicting the duration of trips for new data

### Results:  
The best results were obtained with the Gradient Boosting model

|	|model	                            |RMSLE_train_score	|RMSLE_valid_score |
|--	|---------------------------------- |:-----------------:| ----------------:|
|0	|Linear regression	                |0.54	            |0.54			   |	
|1	|Poly sklearn	                    |0.47	            |0.70			   |	
|2	|Poly sklearn+L2	                |0.48	            |0.48			   |	
|3	|DecisionTreeRegressor	            |0.00	            |0.57			   |	
|4	|DecisionTreeRegressor - maxd11	    |0.41	            |0.43			   |	
|5	|Random Forest	                    |0.40	            |0.41			   |	
|6	|GradientBoostingRegressor	        |0.37	            |0.39			   |	

### Conclusions:  
The RMSLE error on the Kaggle training set was less than 0.4 using the gradient boosting model.
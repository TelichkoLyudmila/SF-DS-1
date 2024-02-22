# Gas Production Forecast using Linear Methods

## Table of Contents
1. Project Description
2. Problem Statement
3. Data Overview
4. Workflow Stages
5. Results
6. Conclusions

### Project Description
We have a dataset on gas production from wells. When opening new wells, it's essential to estimate the revenue each subsequent well will bring and understand which factors (well characteristics) might have the most significant impact on the gas production volume.

### Problem Statement
The goal of the project is to build a regression model that predicts the gas production volume per well (target variable — Prod) based on other well characteristics, and interpret the results of the model.

**Quality Metrics**
MAE, MAPE, coefficient of determination R^2

### Data Overview
The data is presented in a CSV format, containing information about 200 wells for gas production. Features in the data include porosity, permeability, acoustic impedance, brittleness coefficient, total organic carbon, and others.

### Workflow Stages
The project is divided into two parts:
1. Building a simple linear regression model, analyzing the results, and selecting the most significant factors for prediction.
2. Constructing a polynomial regression model with regularization and analyzing the final modeling results.

### Results

|	|model	                            |hyperparameters	|poly              |poMAPE_train_scorely   |MAPE_valid_score   |
|--	|:---------------------------------:|:-----------------:|:----------------:|:---------------------:|:-----------------:|
|0	|Linear all factors	                |None	            |False			   |3.983				   |NaN		    	   |
|1	|Linear crossed factors	            |None	            |False			   |5.025 			       |NaN		     	   |
|2	|Linear skylearn	                |None	            |False			   |4.044				   |NaN			       |
|3	|Poly skylearn	                    |None	            |True			   |1.770				   |2.68			   |
|4	|Poly skylearn+L1                   |L1	                |True			   |1.830				   |2.28			   |
|5	|Poly skylearn+L2                   |L2	                |True			   |1.770				   |2.67			   |
|6	|Poly skylearn+ElasticNet           |ElasticNet         |True			   |2.530				   |3.49			   |

### Conclusions
The best results are achieved using the polynomial model from the scikit-learn library with L1 regularization. Despite the fact that the first three models were not validated, the advantage of the fourth model is evident even on the training set and is maintained on the validation set.
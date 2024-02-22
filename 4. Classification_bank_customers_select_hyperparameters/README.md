# 4. Classification Task, Hyperparameter Tuning for Bank Data

## Table of Contents  
1. Project Description
2. Problem Statement
3. Brief Data Overview
4. Project Workflow
5. Results 
6. Conclusions

### Project Description    
The task is to preprocess data for machine learning, encode them, select the best model for prediction using test and training datasets, and fine-tune hyperparameters.

### Problem Statement    

1. Primary data processing
2. Exploratory Data Analysis (EDA)
3. Feature selection and transformation
4. Classification task: logistic regression and decision trees
5. Classification task: model ensembles and prediction building
6. Hyperparameter tuning

**Competition Conditions:**  
Identify characteristics that can reveal clients more likely to open a bank deposit, and improve the effectiveness of the marketing campaign.

**Quality Metric**     
Improve target metrics, specifically accuracy and F1.

**Practiced Techniques**     
Machine learning methods, model selection

### Brief Data Overview
Data from SkillFactory: 
Information about the bank's last marketing campaign aimed at attracting clients to open a deposit.

### Project Workflow  
1. Primary data processing - cleaning, feature engineering
2. Exploratory Data Analysis (EDA) - statistical significance, correlation, encoding
3. Feature selection and transformation - selecting the most significant, eliminating multicollinearity
4. Classification task: logistic regression and decision trees
5. Classification task: model ensembles and prediction building, hyperparameter tuning

### Results:  
The best results were obtained with the random forest model and hyperparameter tuning.

### Conclusions:  
Using the random forest model and hyperparameter tuning, it was possible to predict whether a client would agree to a deposit campaign with an accuracy of 0.827 and an f1_score of 0.818 on the test set.
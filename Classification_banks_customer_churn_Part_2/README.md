# Churn Prediction in Banking - Classification Task

## Table of Contents
1. Project Description
2. Problem Statement
3. Brief Data Overview
4. Project Workflow
5. Results
6. Conclusions

### Project Description

A bank wants to develop a customer retention loyalty campaign. To achieve this, they want to forecast the probabilities of customer churn and determine if a customer will leave in the near future.

### Problem Statement

Build a classifier that can timely identify departing bank customers, assess the quality of the constructed models, and interpret the results.

**Competition Conditions:**
Best metric performance

**Quality Metric:**
We will use F1 — the weighted average harmonic mean between precision and recall. Precision shows how many of the predicted positive objects are actually positive, and recall shows how many positive objects the model found among all positive objects.

The closer precision is to 1, the less likely the model is to make a type I error, and the closer recall is to 1, the less likely the model is to make a type II error. Thus, the weighted F1 will help find the point where the overall type I and II errors are minimized.

**Practiced Techniques:**
Feature engineering, classification: logistic, polynomial regression, decision trees, random forest, threshold tuning.

### Brief Data Overview

The data is in CSV format and includes the following fields:

- RowNumber — row number;
- CustomerId — customer ID;
- Surname — customer surname;
- CreditScore — credit score;
- Geography — customer's location country;
- Gender — customer gender;
- Age — customer age;
- Tenure — time of using bank services;
- Balance — current account balance;
- NumOfProducts — number of used products;
- HasCrCard — whether there is a credit card;
- IsActiveMember — whether the customer uses bank products more than once a month;
- EstimatedSalary — expected salary;
- Exited — target variable - whether the customer left or stayed.

### Project Workflow

1. Exploratory data analysis.
2. Data preprocessing.
3. Metric selection.
4. Logistic regression.
5. Polynomial regression.
6. Decision trees and random forest.

### Results

As a result, using a random forest with an appropriate threshold value, we managed to achieve the same metric of 0.7 for F1 as in polynomial regression. The precision indicator became slightly higher (in polynomial - 0.6), and recall lower (in polynomial - 0.84). They became a bit closer, which is better for the model: a higher Precision indicates that there is less chance the model will make a type I error, i.e., misclassify loyal customers as churned. A slight decrease in recall indicates that the model's chance of making a type II error has increased, i.e., not "catching" customers who plan to leave the bank and mistakenly classifying them as loyal. However, the metric is still quite high.

### Conclusions

Polynomial regression and random forest showed the best results. The precision indicator in the second case became slightly higher, and recall lower. Depending on the bank's goals, one of these two models can be used.
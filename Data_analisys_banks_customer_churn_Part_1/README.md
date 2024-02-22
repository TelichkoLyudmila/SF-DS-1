# Customer Relationship Analysis in a Bank - Preliminary Analysis and Visualization

## Table of Contents
1. Project Description
2. Problem Statement
3. Data Overview
4. Workflow Stages
5. Results
6. Conclusions

### Project Description
A bank intends to develop a customer retention loyalty campaign. To achieve this, the bank aims to predict the probabilities of customer churn and determine whether a customer will leave in the near future.

### Problem Statement
Task: Identify relationships in the data and build visualizations.

**Practiced Skills**
Feature engineering, plotly and matplotlib.pyplot visualization

### Data Overview
The data is presented in a CSV format with the following columns:

- RowNumber — row number;
- CustomerId — customer ID;
- Surname — customer's surname;
- CreditScore — credit rating;
- Geography — customer's country;
- Gender — customer's gender;
- Age — customer's age;
- Tenure — time with the bank;
- Balance — current account balance;
- NumOfProducts — number of bank products used;
- HasCrCard — whether the customer has a credit card;
- IsActiveMember — whether the customer uses bank products more than once a month;
- EstimatedSalary — expected salary;
- Exited — target variable - whether the customer left or stayed.

### Workflow Stages

- What is the ratio of churned and loyal customers?
- Examine the balance distribution of users with balances over $2,500.
- Examine the balance distribution of customers in terms of churn.
- Examine the age distribution in terms of churn.
- Build a plot showing the relationship between the customer's credit rating and their estimated salary.
- Who leaves more often, men or women?
- How does customer churn depend on the number of bank services acquired?
- How does the presence of an active customer status affect customer churn?
- In which country is the proportion of departed customers higher?

### Results

Some relationships in customer data have been examined:

- What is the ratio of churned and loyal customers?

The proportion of loyal customers is significantly higher, accounting for almost 80%. Interestingly, around 5% of loyal customers have near-zero balances.

- Examine the balance distribution of users with balances over $2,500.

Most users have balances ranging from $100 to $140k. Balances exceeding $200k are rare, suggesting that larger amounts are transferred to other products where they do not appear in the sample. The distribution is close to normal.

- Examine the balance distribution of customers in terms of churn.

Churned customers exhibit a more significant balance dispersion. This suggests that the bank may have specific benefits/requirements regarding maintaining a certain balance. Customers who exceed or fall below the required sum may not receive favorable conditions and thus leave.

- Examine the age distribution in terms of churn.

The majority of loyal customers fall into the 30-40 age category, while individuals aged 40-50 tend to leave. Most outliers among loyal customers are also near retirement age. The bank might consider special programs for retirees or low-risk products for those over 40, who often have accumulated capital.

- Build a plot showing the relationship between the customer's credit rating and their estimated salary.

It's evident that approximately one-third of churned customers had a significantly lower credit rating, indicating possible rejections for certain credit products, contributing to their departure. Among loyal customers, the majority have average ratings (500 to 700 points).

- Who leaves more often, men or women?

Women tend to leave slightly more.

- How does customer churn depend on the number of bank services acquired?

On average, loyal customers had more bank products. Looking at the median value, loyal customers had 2 products, while churned customers had 1. However, when considering the average per person in the groups, the difference is not significant: loyal - 1.54, churned - 1.48.

Potential conclusion: A significant number of departed customers only used one bank product. The situation is quite bleak for customers who used 3 and 4 products; there the proportion of departed customers significantly exceeds loyal ones, reaching 100% with 4 products.

- How does the presence of an active customer status affect customer churn?

On average, in the group of loyal customers, one out of two people is an active user. In the churned group, only one out of three people is active. If customers do not use the bank's services, they will leave at some point. The bank may consider running promotions or offering specialized products to inactive customers.

- In which country is the proportion of departed customers higher?

Most customers leave from Germany, where every third customer has already left. Either the bank is not winning in the competitive struggle in the country, or the conditions are too restrictive for German citizens.

### Conclusions

The majority of departing customers in the bank are recent customers with the lowest credit rating - these customers should not be retained as they represent natural turnover for the bank. However, the second-largest category is customers who have been with the bank for over 10 years; they may fall into the low credit rating category due to pre-pension age and lack of regular income. It might be worth thoroughly checking such customers. Additionally, every fourth new customer and 10-year customer with a high rating leave the bank, indicating insufficiently good programs for these customer categories.
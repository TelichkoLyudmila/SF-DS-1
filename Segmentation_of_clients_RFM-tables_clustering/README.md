# Project 6. Customer Segmentation of an Online Store Using RFM Table

## Table of Contents  
[1. Project Description](.README.md#project-description)  
[2. Problem Statement](.README.md#problem-statement)  
[3. Brief Data Overview](.README.md#brief-data-overview)  
[4. Project Workflow](.README.md#project-workflow)  
[5. Results](.README.md#results)    
[6. Conclusions](.README.md#conclusions) 

### Project Description    
  
The essence of the case is to solve a marketing task: segment existing customers by building an RFM table and interpret these segments.

### Problem Statement    
Transform the raw data and build a customer clustering model based on their purchasing power, order frequency, and recency of the last purchase. Determine the profile of each cluster.

**Competition Conditions:**  
Quality of clustering segments for marketing purposes

**Quality Metric**     
Silhouette coefficient and the ability to use clustering for marketing purposes

**Practiced Techniques**     
Feature engineering, clustering

### Brief Data Overview
The data is presented in a CSV table, where each row contains information about a unique transaction.
Features describing each transaction:

- InvoiceNo — invoice number (a unique nominal six-digit number assigned to each transaction; the letter 'C' at the beginning of the code indicates a transaction cancellation);
- StockCode — product code (a unique five-digit integer assigned to each individual product);
- Description — product name;
- Quantity — quantity of each product per transaction;
- InvoiceDate — date and time of invoicing/transaction;
- UnitPrice — price per unit of product in pounds;
- CustomerID — customer identifier (a unique five-digit number assigned to each customer);
- Country — name of the country where the customer resides.

### Project Workflow  
1. Familiarity with the data structure
2. Transformation, cleaning, and analysis of data
3. Exploratory data analysis of transaction data
4. Building an RFM table and identifying RFM outliers
5. Modeling and evaluating model quality

### Results:  

Using KMeans clustering initially formed 4 groups of customers:
- dormant (many purchases but a long time ago),
- loyal (frequent and active buyers),
- newcomers (infrequent but recent),
- those who spent the most money and therefore stand out (something like VIP clients).

However, later, with the help of the non-linear dimensionality reduction method t-SNE, a more detailed separation into clusters was achieved. In the case of 2 main components - 6 clusters and in the case of 3 - 10 clusters.

- in the case of 6 clusters, "loyal" are highlighted as one cluster, while when divided into 10 clusters, they are split into "loyal" and "VIP".
- "promising" and "newcomers" are clearly defined in the case of 6 clusters, while in a more detailed breakdown among "newcomers" there are variations.
- if more than 150 days have passed since the last order, both approaches form 2 different clusters of "dormant".
- "drifting" and "at risk" are quite clearly defined in both approaches.

Summing up, it can be said that the t-SNE dimensionality reduction method in conjunction with KMeans performed well and allowed for the formation of quite clear clusters in conditions where they are clearly not separated. Depending on marketing goals, both more detailed and less detailed clustering can be used.

### Conclusions:  
It was possible to form clusters in such a way that, in the end, a separate marketing strategy could be chosen for each group of customers. Depending on the marketing goals, a more or less detailed clustering can be chosen.
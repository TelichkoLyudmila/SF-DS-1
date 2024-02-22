# 8. Final Project. Brief for "Civil Society Research Laboratory". Identification of Vulnerable Population Groups

## Table of Contents  
1. Project Description
2. Problem Statement
3. Brief Data Overview
4. Project Workflow
5. Results
6. Conclusions

### Project Description    
  
Until 2021, the "poverty line" (living below the subsistence minimum) in Russia was determined by the cost of the minimum food basket. In the same year, the government "decoupled" the poverty level from prices for basic products: from 2021, the subsistence minimum is calculated as 44.2% of the median income of Russian citizens for the previous year.

In this regard, it is necessary to use clustering to identify which regions fall into the most vulnerable population groups.

### Problem Statement    

Using machine learning methods to identify regions most in need of social support based on publicly available data from government statistics.

**Competition Conditions:**  
It is necessary to:
- cluster the regions of Russia and determine which of them most
urgently need help for the low-income/disadvantaged
population strata;
- describe the population groups facing poverty;
- determine:
    - whether the number of children, pensioners, and other socially vulnerable
groups affect the poverty level in the region;
    - whether the level of poverty/social distress is related to
production and consumption in the region;
    - what other dependencies can be observed regarding
socially unprotected population strata.

**Quality Metric**     
Silhouette coefficient and the ability to use clustering for project purposes

**Practiced Techniques**     
Feature engineering, standardization, clustering, visualization (including by geotags)

### Brief Data Overview
Data is collected from official statistics for 2017-2022. For some indicators, as of 31.01.2024, there was no data for 2022.

- child_mortality_rural - The number of infants who died in the first year of life per year (people) in rural areas
- child_mortality_urban - The number of infants who died in the first year of life per year (people) in urban areas
- nominal_income - Average per capita monetary income (monthly), rubles
- real_income_to_previos_year - Real monetary income as a percentage of the previous year		
- avg_population - Average population over the year		
- disability - Total number of disabled people	
- disease - Incidence per 1000 people	
- gross_regional_product - Gross regional product per capita before 2021	
- housing_on_one_person - Total area of residential premises per capita (sq. m.)
- natural_population_groth - Natural growth per year	
- people_lower_poverty_line - Number of people with incomes below the poverty line
- disabled_population - Share of the disabled population in the regions
	- poverty_socdem_2017 - 2021 - Distribution of the low-income population by socio-demographic groups (percentage, indicator value for the year)
- retail_turnover_per_capita - Retail trade turnover per capita (rubles, indicator value for the year)
- unemployed - Number of unemployed citizens registered with state employment services and receiving social benefits (people)
- workers - Ratio of the number of employed in the region's economy to the population of the region in working age (percentage)
- welfare_expense_share - Share of expenditures on social policy in the total volume of expenditures of consolidated budgets of the subjects of the Russian Federation (in %)
- crime_total - Total registered crimes	
- crime_economical - Persons detected committing economic crimes	
- crime_without_income  - Persons detected committing crimes without a permanent source of income

### Project Workflow  
1. Data Collection and Processing. \
1.1. Import and standardization of column names\
1.2. Selection of necessary regions, standardization of names\
1.3. Merging into a single dataset\
1.4. Handling missing values\
1.5. Dataset with relative values\
1.6. Standardization of all features to the "the more, the better" format\
1.7. Formation of datasets for each year
2. Exploratory Data Analysis\
2.1. Key descriptive statistics\
2.2. Visualization of relative features\
2.3. Visualization of absolute features\
2.4. Regions with problems in the majority of features
3. Analysis of Feature Interdependencies\
3.1. Correlation matrix for the dataset with relative features\
3.2. Correlation matrix for the dataset with absolute features\
3.3. Preparation for clustering - standardization
4. Clustering\
4.1. K-means\
4.2. Hierarchical clustering\
4.3. DBSCAN\
4.4. Dimensionality reduction - PCA\
4.4.1 PCA - K-means\
4.4.2 PCA - Hierarchical clustering\
4.5 Dimensionality reduction t-SNE\
4.5.1 t-SNE - K-means\
4.5.2 t-SNE - Hierarchical clustering\
4.6 Summary of clustering results
5. Clustering for all years of observations\
5.1. Clustering for 2017-2022\
5.2. Map with clustering of regions in the Russian Federation
6. Conclusions

### Results:  

During the project, fresh social statistics were downloaded from the Rosstat and fedstat websites. After cleaning and processing the data, 19 datasets with regions for the period 2017-2022 were obtained. Here, we faced the challenge that we essentially have features for clustering regions and time series simultaneously. It could have been possible to perform time series clustering for each feature, which would allow tracking certain patterns: whether identical values are reached over time, whether there are similar trends towards simultaneous increase and decrease, or similar repeating patterns in different years. However, since we have weather statistics, and the time series is not very long (from 2017 - the year of Rosstat's methodology change), time series clustering would not be very productive. Therefore, we considered clustering regions based on features.

For the final clustering, separate datasets for 2017-2022 were obtained, within each of which there were tables Regions/features. Also, for the main analyzing dataset (on which clustering methods were tested), a dataset based on the average feature for the last 3 years (2020-2022) was taken. These years covered the pandemic and the beginning of the economic crisis, so they should fairly clearly identify regions in need. Also, considering that some features were in natural (absolute) expression, i.e., in people, it was obvious that features tied to the population size would strongly correlate. Therefore, separate datasets were created for each year with relative features (i.e., divided by the population).

### Conclusions:  
The following interdependencies between the data were identified:
- A cross-correlation above 90% between the features "Share of disabled population" and "Share of population with incomes below the poverty line." This indicates a high likelihood that these two features are related, as the distribution of regions based on them is almost identical. Therefore, it can be concluded that regions with a higher proportion of elderly and children face a significant burden for families, pushing them below the poverty line per person. Undoubtedly, such regions are in great need of social support.
- An 80% correlation between the features "Ratio of employed in the region's economy to the population of the region in working age" and "Average per capita monetary income" - this also seems logical because the more people who have the opportunity to work, the higher the average per capita income (since the calculation of this indicator includes the total population, not just the employed population). A similar high correlation between workers and Gross Regional Product (GRP) - the explanation principle is the same (the more workers, the higher the GRP per capita). Some of these features may be excluded in the future, as they generally explain regions in a similar way.
- Less than 90%, but also a high reverse correlation between the features "Total area of residential premises per capita" and "Natural population growth rate." That is, the more population decline, the more square meters per person - this looks reasonable.
- Interesting relationship with the feature "welfare_expense_share" (Share of expenditures on social policy in the total volume of expenditures of consolidated budgets of the subjects of the Russian Federation): moderately high inverse correlation with the features of average per capita income, GRP, and the share of the working population of working age (these indicators are also highly correlated with each other). It can be assumed that social support is largely distributed based on this official statistics.
- The population with incomes below the poverty line has a fairly high inverse correlation with retail trade turnover per capita. In general, this looks logical: the lower the income level in the region, the smaller the contribution to the region's development (including trade) that the population makes.
- The larger the population, the more crimes in absolute terms. Note that the average inverse correlation is observed between this feature and all three types of crimes, which is generally explainable, considering the negative natural population growth.

Before starting the clustering, regions that fell into the bottom 10% of each feature were identified (i.e., regions with the most dismal situation for each feature). At this stage, we noticed that in addition to subsidized regions, the Nenets Autonomous Okrug fell into the list. After conducting clustering, we obtained very similar results: the same subsidized regions, Nenets and Yamalo-Nenets Autonomous Okrug, fell into the two smallest classes. Many of them lead in indicators such as minimum income per capita, minimum area per person, maximum child mortality, diseases, and many other indicators.

As for the Nenets and Yamalo-Nenets Autonomous Okrugs - despite being resource-rich regions with high per capita income linked to extracted minerals (they are in the top for the highest GRP per capita), these are regions with a very high cost of living and high social problems per region's small population. Surprisingly, these same regions lead in the share of disabled people in the population. Nenets Region enters the 10% worst by indicators of disease rate per 1000 people, the total number of disabled people, the proportion of people below the poverty line, and economic crimes. And the Yamalo-Nenets Autonomous Okrug is in the same top for diseases and minimum housing availability. Also, both of these regions are in the 10% minimum percentages for social support allocated from the region's funds. Essentially, a somewhat unexpected conclusion is that a region can have high GRP and income per capita but, due to other factors (not considered in social payments), may need additional support for the population. **As a result, regions that, based on the results of the research, require more support for the population than others have been identified: Kamchatka Krai, Magadan Oblast, Nenets Autonomous Okrug, Altai Republic, Ingushetia Republic, Tuva Republic, Chechen Republic, Chukotka Autonomous Okrug, Yamalo-Nenets Autonomous Okrug.**




